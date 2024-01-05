# follow these instructions to enable usage of kaggle api
# https://www.kaggle.com/datasets/andrewmvd/road-sign-detection

# if [ -f "~/.kaggle/kaggle.json" ]; then
#     echo "Kaggle JSON file exists"
# else
#     echo "Kaggle JSON file does not exist"
#     echo "Follow these instructions to use the Kaggle API"
#     echo "https://www.kaggle.com/datasets/andrewmvd/road-sign-detection"
#     exit
# fi

mkdir -p 'DataOriginal/RoadSign'
kaggle datasets download andrewmvd/road-sign-detection --unzip -p DataOriginal/RoadSign