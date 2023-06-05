from ultralytics import YOLO

model = YOLO("yolov8n.pt")


from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()
root_path = file_path.parent
print("file path ",file_path)
results=model.train(data=str(root_path)+"/custom_data.yaml",
                    epochs=1,save=True)