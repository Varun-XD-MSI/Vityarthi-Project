from ultralytics import YOLO

# Load the trained model (.pt file)
model = YOLO("Vityarthi-Project/best.pt")

# Run inference on a test image
results = model("Vityarthi-Project/test_images/00066_278.jpg")

# Display the detection results
results[0].show()
