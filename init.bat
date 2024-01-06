@echo off

REM "https://github.com/Kaggle/kaggle-api#api-credentials"
mkdir "DataOriginal/RoadSign"
mkdir "DataOriginal/TrafficSignYolo"
mkdir "DataOriginal/RoadSignDetection"

@echo on
kaggle datasets download andrewmvd/road-sign-detection --unzip -p DataOriginal/RoadSign
kaggle datasets download pkdarabi/traffic-signs-detection-using-yolov8 --unzip -p DataOriginal/TrafficSignYolo