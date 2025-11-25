from ultralytics import YOLO

# Load the trained model (.pt file)
model = YOLO("best.pt")

# Run inference on a test image
results = model("test_images/00066_278.jpg")

# Display the detection results
results[0].show()
