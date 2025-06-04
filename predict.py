import cv2
from ultralytics import YOLO
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()    # 在 Windows 上运行多进程必需
    # Load a pretrained YOLO11n model
    model = YOLO("yolo11n.pt")

    # Define path to the image file
    source = "./images/su7.png"

    # Run inference on the source
    results = model.predict(source, save=True, show=True)
    cv2.waitKey()
