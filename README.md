# 🧠 Brain Tumor Detection using YOLOv12

---

## 📌 Project Title
**Brain Tumor Detection using YOLOv12 (Deep Learning – Object Detection)**

---

## 📘 Overview of the Project
This project uses **YOLOv12**, a state-of-the-art object detection model, to automatically detect brain tumors from MRI images.  
The aim is to create a fast, accurate, and easy-to-use AI system that helps in medical image analysis by identifying tumor regions in MRI scans.

The repository includes:
- A trained YOLOv12 model (`best.pt`)
- A test script (`test.py`)
- Training source code (`Source.py`)
- Sample MRI images
- Project documentation (`Statement.md`)

---

## ⭐ Features
- Detects **tumor / no tumor** from MRI scans  
- Powered by **YOLOv12** for high detection accuracy  
- Pretrained `best.pt` model included  
- Simple inference using `test.py`  
- Contains sample images for quick testing  
- Works on **local system** and **Google Colab**

---

## 🧰 Technologies / Tools Used
- **Python 3**
- **Ultralytics YOLOv12**
- **PyTorch**
- **OpenCV**
- **NumPy**
- **Google Colab**
- **GitHub**

---

## 🛠️ Steps to Install & Run the Project

### **1. Clone the repository using terminal**
```bash
git clone https://github.com/Varun-XD-MSI/Vityarthi-Project     
cd Vityarthi-Project                                             
```
### **2. Install required dependencies**
```bash
pip install ultralytics opencv-python pillow numpy
```
### **3. Add and run this in your dedicated python file**
```bash
from ultralytics import YOLO

# Load the trained model (.pt file)
model = YOLO("Vityarthi-Project/best.pt")

# Run inference on a test image
results = model("Vityarthi-Project/test_images/00066_278.jpg")  #Use correct path here!!!

# Display the detection results
results[0].show()
```
### 4. Output


**The script will:**

-**Load best.pt**

**-Run YOLOv12 inference**

**-Display an MRI image with a bounding box and confidence score**

---




**🖼️ Screenshots**

<img width="1342" height="798" alt="image" src="https://github.com/user-attachments/assets/460d51a0-b242-4128-86fc-3919b7c2021c" />
<br><br/>

<img width="1071" height="65" alt="image" src="https://github.com/user-attachments/assets/0b0a3561-9b08-429c-82e2-69edcadf996d" />
<br><br/>

---






<img width="1468" height="873" alt="image" src="https://github.com/user-attachments/assets/09c22aba-7cab-43bc-a6c7-ac435723a918" />
<br><br/>
<img width="1086" height="69" alt="image" src="https://github.com/user-attachments/assets/844c029c-9816-430d-a296-f4dea342e5d8" />



