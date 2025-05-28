from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # TODO 指向自己训练的模型

# Customize validation settings
metrics = model.val(data="./data/data.yaml", imgsz=640, batch=16, conf=0.25, iou=0.6, device="0")