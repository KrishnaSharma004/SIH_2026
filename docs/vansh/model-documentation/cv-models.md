# Computer Vision Model Documentation

## Project
AI-Powered Mobile Urban Intelligence Platform Using Public Transport Fleet

## Developer
Vansh

---

# 1. YOLO11n — General Object Detection

### Model
YOLO11n

### Purpose
Used as the initial baseline model for detecting general objects in road/urban scenes.

### Why Used
- Lightweight model
- Fast inference
- Suitable for real-time Computer Vision experimentation
- Easy integration with the Ultralytics framework
- Useful as a baseline before training project-specific models

### Current Use
The model is currently used for baseline detection of objects such as:

- Cars
- Buses
- Persons
- Other supported general object classes

### Input
Image or video frame.

### Output
For each detected object:

- Class ID
- Class name
- Confidence score
- Bounding box coordinates

### Current Status
Baseline inference verified successfully.

---

# 2. YOLO11 Face Detection Model

### Model File
`cv/models/yolov11n-face.pt`

### Purpose
Detect faces in captured frames so that identifiable facial information can be anonymized.

### Why Used
The SIH system may process public-road video containing pedestrians and passengers. Faces should not be unnecessarily stored as identifiable visual data.

### Processing
1. Detect face
2. Extract face bounding box
3. Apply Gaussian blur
4. Continue with downstream Computer Vision processing

### Privacy Approach

Raw frame
→ Face Detection
→ Face Blur
→ Privacy-Safe Frame
→ Object Detection / Further Processing

### Current Status
Face detection and anonymization successfully verified.

---

# 3. Ultralytics YOLO Framework

### Purpose
Provides the framework used to load, run and test YOLO models.

### Current Environment

- Ultralytics: 8.4.138
- PyTorch: 2.14.0+cpu
- Python: 3.11.6
- OpenCV: 5.0.0

### Hardware

- CPU: AMD Ryzen 5 5500U
- GPU: No dedicated NVIDIA GPU
- Current development: CPU-based

### Role in Project

The framework will later be used for:

- Road-defect detection
- Vehicle detection
- Pedestrian detection
- Traffic-sign detection
- Model training
- Model validation
- Model inference
- Edge optimization

---

# 4. Current Model Strategy

The current models are baseline models.

They are not considered the final SIH models.

Project-specific models will be trained/fine-tuned using suitable road and infrastructure datasets.

Planned model areas include:

- Pothole detection
- Road cracks/damage
- Waterlogging
- Missing road dividers
- Missing zebra crossings
- Traffic-sign detection
- Vehicle classification
- Pedestrian detection

---

# 5. Model Development Direction

Baseline
→ Dataset Preparation
→ Annotation Verification
→ Model Training
→ Validation
→ Evaluation
→ Optimization
→ Edge Deployment

The final Computer Vision system should provide reliable detections that can be converted into georeferenced events for the central urban intelligence platform.