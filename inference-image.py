import cv2
from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Define path to the image file
source = "res/su7.png"

# Run inference on the source
results = model.predict(source, save=True, show=True)
cv2.waitKey()
