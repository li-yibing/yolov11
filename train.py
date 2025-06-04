from ultralytics import YOLO
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()    # 在 Windows 上运行多进程必需
    # Load a model
    model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data="./datasets/data.yaml", epochs=100, imgsz=640, batch=16, workers=1)