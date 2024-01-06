from ultralytics import YOLO
import torch


if __name__ == '__main__':
    model = YOLO('traffic_sign.pt')
    model.to('cuda')
    
    model.predict(source='test2.png.jpg', save=True, show=True)