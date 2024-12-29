from ultralytics import YOLO

# 加載訓練好的 YOLO 模型
model = YOLO(r"runs\detect\train7\weights\best.pt")  # 替換為你的模型路徑

# 指定要處理的圖片或資料夾
source = r"dataset\train\plastic"  # 單張圖片或包含多張圖片的資料夾

# 執行預測
results = model.predict(
    source=source,          # 輸入圖片或資料夾
    save=True,              # 保存結果圖片
    save_txt=True,          # 保存 YOLO 格式的標籤 (.txt 文件)
    conf=0.5,               # 設置置信度閾值
    iou=0.5                 # 設置 IOU 閾值
)

# # 獲取預測結果
# for result in results:
#     print(result)  # 每個 result 包含框、類別、分數等資訊

# for result in results:
#     boxes = result.boxes.xyxy.cpu().numpy()  # 獲取框座標 (x_min, y_min, x_max, y_max)
#     classes = result.boxes.cls.cpu().numpy()  # 獲取類別 ID
#     confidences = result.boxes.conf.cpu().numpy()  # 獲取置信度

#     print("Boxes:", boxes)
#     print("Classes:", classes)
#     print("Confidences:", confidences)

import cv2

for result in results:
    img = cv2.imread(result.path)  # 讀取原圖
    for box, cls, conf in zip(result.boxes.xyxy, result.boxes.cls, result.boxes.conf):
        box = box.cpu().numpy().astype(int)
        cls = int(cls)
        conf = float(conf)
        # 畫出框
        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
        # 加入類別與置信度
        cv2.putText(img, f"Class {cls} {conf:.2f}", (box[0], box[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 保存或顯示圖片
    cv2.imwrite(f"output_{result.path.split('/')[-1]}", img)
