from ultralytics import YOLO
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()    # 在 Windows 上运行多进程必需
    # Load a model
    model = YOLO("runs/detect/train33/weights/best.pt")  # TODO 指向自己训练的模型

    # Customize validation settings
    metrics = model.val()
    results = model.predict("datasets/test/images", save=True, workers=1, conf=0.25, iou=0.65, save_txt=True, save_conf=True)