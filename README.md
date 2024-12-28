# 專題: 垃圾分類
將垃圾分辨是否為一般垃圾或是回收垃圾，並提示用戶要將垃圾會是屬於什麼

![image](https://github.com/davidcheng220/trash-system/blob/main/img/image.png)

# 垃圾分類共有:
* metal(鋁箔包)
* glass(玻璃瓶)
* paper(紙)
* plastic(塑膠瓶)
* papercup(手搖)
* trash(一般)

# 會有甚麼
* OpenCV
* YoloV11
* TensorFlow
* MySQL
* Flask
* Fast API
* Raspberry pi (ESP32/Jetson Nano)
* AWS (Cloud computing)
* 垃圾滿不滿
* Prediction (預測垃圾會在甚麼時候滿)

# Requirements:
>* Pyhton 3.8 or later
>* Virtual environment

# Create Python venv
```
python -m venv venv
.\venv\Script\activate
or
source venv\bin\activate
```

# Install Requirements
```
pip install -r requirements.txt
```
後面待補充
# Label Studio 使用教學
Download docker-compose.yml，建立一個資料夾用來放docker-compose.yml，在資料夾中新增2個資料夾mydata、myfiles<br/>
打開終端機，cd至docker-compose.yml的所在資料夾<br/>
輸入指令<br/>
```
docker-compose up
```
打開docker desktop，找到label-studio容器<br/>
點擊port開啟local host瀏覽，建立帳號登入<br/>
create new project，到Labeling Setup，點選Object Detection with Bounding Boxes<br/>
把預設的labels刪除，加入labels，完成後按save<br/>
點選import上傳圖片，點選圖片進入標記頁面<br/>
點選你要標記的label，在圖片上框出位置(可以多個種類多個框)<br/>
做完後點選export，選擇要輸出的檔案類型
