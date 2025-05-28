from ultralytics import YOLO

# Load a model
model = YOLO("runs/detect/train3/weights/best.pt")  # TODO 指向自己训练的模型

# Customize validation settings
metrics = model.val()
results = model.predict("datasets/images/test", save=True)