🧠 Brain Tumor Detection using YOLOv12

A deep-learning model trained to detect brain tumors using the latest YOLOv12 architecture.
This repository contains the trained model, inference notebook, and sample test images for quick evaluation.


Project Structure
├── best.pt                 # Trained YOLOv12 model
├── Brain_tumor.ipynb       # Training notebook
├── Test.ipynb              # Inference notebook (runs predictions)
├── test_images/            # Sample test images
├── README.md               # Project documentation



⚙️ Requirements

This project runs on Google Colab or locally with:

Python 3.10+

PyTorch (CUDA recommended)

Ultralytics YOLOv12

Install YOLOv12 using:

pip install ultralytics




🚀 Running Inference (Predict Tumor)

You can run predictions in Test.ipynb.

Example inference code:

from ultralytics import YOLO

# Load trained model
model = YOLO("best.pt")

# Predict on an image
results = model("test_images/test1.jpg")

# Display result
results[0].show()






📦 Running Locally

Clone the repo:

git clone https://github.com/Varun-XD-MSI/Tumor-detection-vityarthi.git
cd Tumor-detection-vityarthi


Run inference:

python inference.py --image test_images/sample.jpg --model best.pt




📁 Test Images

A folder test_images/ is included so anyone can run the model immediately.

You can add your own MRI scans here:

test_images/
├── test1.jpg
├── test2.jpg




🧩 What This Model Does

✔ Detects presence of a tumor
✔ Localizes the tumor region with bounding boxes
✔ Trained on MRI brain scans

🙌 Credits

YOLOv12 by Ultralytics

Dataset: Brain MRI Tumor Dataset 
