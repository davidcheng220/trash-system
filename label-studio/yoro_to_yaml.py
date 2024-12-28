import os

# 設定 Label Studio 輸出的資料夾
output_dir = "path/to/labelstudio/output"
images_dir = os.path.join(output_dir, "images")
labels_dir = os.path.join(output_dir, "labels")
classes_file = os.path.join(output_dir, "classes.txt")

# 設定 YAML 檔案的路徑
yaml_path = "dataset.yaml"

# 讀取類別名稱
with open(classes_file, "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# 確認影像及標註資料夾存在
if not os.path.exists(images_dir):
    raise FileNotFoundError(f"Images directory not found: {images_dir}")
if not os.path.exists(labels_dir):
    raise FileNotFoundError(f"Labels directory not found: {labels_dir}")

# 自動生成 YAML 內容
yaml_content = f"""train: {images_dir}
val: {images_dir}  # 預設將訓練集用作驗證集
nc: {len(class_names)}
names: {class_names}
"""

# 將 YAML 內容寫入檔案
with open(yaml_path, "w") as f:
    f.write(yaml_content)

print(f"YAML file created: {yaml_path}")
