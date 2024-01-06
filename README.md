# Data sets used
https://www.kaggle.com/datasets/andrewmvd/road-sign-detection 
https://www.kaggle.com/datasets/pkdarabi/traffic-signs-detection-using-yolov8

# first execute pip install
pip install -r requirments.txt

# init.sh/init.bat
Linux/Windows scripts respectively to download datasets from kaggle and automatically extract them

# split.py
Seperate data in RoadSign into 80:20 ratio for training and validation

# main.py
Used to train the model 
After training, best.pt file will be generated in the latest weight folder under the latest runs/detect/train folder
copy best.pt to parent folder and rename it to traffic-sign.pt

# videocam.py
Opens a streamlit app in the browser and detects traffic signals like speed limit, greeen or red lights
Open using `streamlit run videocam.py`
