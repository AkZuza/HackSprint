# follow these instructions to enable usage of kaggle api
# https://github.com/Kaggle/kaggle-api#api-credentials

# if [ -f "~/.kaggle/kaggle.json" ]; then
#     echo "Kaggle JSON file exists"
# else
#     echo "Kaggle JSON file does not exist"
#     echo "Follow these instructions to use the Kaggle API"
#     echo "https://github.com/Kaggle/kaggle-api#api-credentials"
#     exit
# fi

mkdir -p 'DataOriginal/RoadSign'
mkdir -p "Data/TrafficRoadSign"
kaggle datasets download andrewmvd/road-sign-detection --unzip -p DataOriginal/RoadSign
kaggle datasets download pkdarabi/traffic-signs-detection-using-yolov8 --unzip -p Data/TrafficRoadSign