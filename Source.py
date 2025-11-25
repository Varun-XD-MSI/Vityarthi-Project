# -*- coding: utf-8 -*-
"""
Training script used in Google Colab.
This file documents how the YOLOv12 model was trained for the project.
"""

from google.colab import drive        # To mount Drive and access dataset
drive.mount('/content/drive')


# Navigate to project directory (uncomment when running in Colab)
# %cd /content/drive/MyDrive/Project


# Clone YOLOv12 repository (executed in Colab using shell command)
# Note: In Colab this must be written as:  !git clone <repo-url>
# Kept here for documentation purpose.
git clone https://github.com/sunsmarterjie/yolov12    # To download YOLOv12 source code


# Enter the YOLOv12 folder
# %cd yolov12


# -------------------------------------------------------------------------
# Remove flash_attn .whl files from requirements.txt
# These wheels are not supported on Google Colab and break installation.
# -------------------------------------------------------------------------
with open("requirements.txt", "r") as f:
    lines = f.readlines()

with open("requirements.txt", "w") as f:
    for line in lines:
        if ".whl" in line and "flash_attn" in line:
            continue  # Skip incompatible flash_attn wheel line
        f.write(line)

print("Fixed requirements.txt — removed incompatible flash_attn wheel.")


# -------------------------------------------------------------------------
# Load YOLO model from the Ultralytics library
# (Used here for demonstration of the training approach)
# -------------------------------------------------------------------------
from ultralytics import YOLO

# Load YOLOv12 small model weights (yolo12s.pt)
model = YOLO('yolo12s.pt')


# -------------------------------------------------------------------------
# Start training with custom dataset (brain tumor dataset)
# These were the training hyperparameters used in the project.
# -------------------------------------------------------------------------
results = model.train(
    data='/content/drive/MyDrive/Project/brain-tumor/brain-tumor.yaml',  # Dataset YAML
    epochs=20,            # Number of training epochs
    batch=64,             # Batch size
    imgsz=640,            # Input image size
    scale=0.5,            # Multi-scale training factor
    mosaic=1.0,           # Mosaic augmentation
    mixup=0.0,            # MixUp augmentation disabled
    copy_paste=0.1,       # Copy-Paste augmentation
    device="0",           # GPU device
)

# End of training script
