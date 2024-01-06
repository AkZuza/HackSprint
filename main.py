from ultralytics import YOLO
import torch


if __name__ == '__main__':
    model = YOLO('yolov8m.pt')
    model.to('cuda')
    
    model.train(source='Data/TrafficRoadSign/data.yaml', workers=8, epochs=100, batch=4, device=1)
    model.val()
    model.export()