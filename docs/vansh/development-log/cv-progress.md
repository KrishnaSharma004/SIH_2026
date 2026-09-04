# Computer Vision Development Progress

## Project
AI-Powered Mobile Urban Intelligence Platform Using Public Transport Fleet

## Developer
Vansh

---

# CV-01 — Computer Vision Environment Setup

### Objective
Set up the Computer Vision development environment for the SIH 2026 project.

### Work Done
- Created the `cv/` module structure.
- Created a dedicated Python virtual environment named `cv_env`.
- Installed and configured Ultralytics YOLO.
- Verified the installation using YOLO environment checks.

### Environment
- Python: 3.11.6
- Ultralytics: 8.4.138
- PyTorch: 2.14.0+cpu
- OpenCV: 5.0.0
- Device: CPU
- GPU: Not available

### Result
Computer Vision development environment was successfully configured and verified.

---

# CV-02 — YOLO Baseline Object Detection

### Objective
Verify that a pretrained YOLO model can perform object detection successfully.

### Work Done
- Used pretrained `YOLO11n` model.
- Tested the model on a sample bus image.
- Verified detection of common objects.

### Detected Objects
- Person
- Bus

### Result
YOLO baseline inference worked successfully on the local CPU environment.

### Observation
The pretrained model can detect general objects, but it does not yet detect project-specific road defects such as potholes.

---

# CV-03 — Reusable Object Detection Module

### Objective
Create a reusable Python module for object detection instead of directly using YOLO commands every time.

### File Created
`cv/inference/detector.py`

### Work Done
- Created `CVDetector` class.
- Added model loading.
- Added image/frame detection method.
- Converted YOLO results into structured detection dictionaries.
- Returned:
  - Class ID
  - Class name
  - Confidence
  - Bounding box coordinates

### Result
A reusable object detection interface was successfully created.

---

# CV-04 — Face Detection and Privacy Anonymization

### Objective
Protect personal privacy by detecting and blurring faces before storing or further processing captured visual data.

### Initial Approach
OpenCV Haar Cascade was initially considered for face detection.

### Problem
The installed OpenCV 5.0.0 environment did not provide the expected `CascadeClassifier` interface.

### Solution
A dedicated YOLO-based face detection model was used:

`cv/models/yolov11n-face.pt`

### Work Done
- Loaded the YOLO face detection model.
- Detected face bounding boxes.
- Applied Gaussian blur to detected face regions.
- Tested the implementation successfully.

### File Created
`cv/privacy/face_blur.py`

### Privacy Principle
Faces should be anonymized before persistent storage or unnecessary transmission.

### Result
Face detection and face anonymization were successfully verified.

---

# CV-05 — Privacy-Aware Video Processing Pipeline

### Objective
Create an end-to-end video pipeline that performs privacy protection and object detection on public-transport/dashcam video.

### Input
Urban dashcam video:

- Resolution: 1920 × 1080
- Frame rate: 30 FPS
- Total frames read: 3601

### Processing Pipeline

Video Input
→ Frame Selection
→ Resize to 640 × 360
→ Face Detection
→ Face Blurring
→ YOLO Object Detection
→ Annotated Output Video

### Optimization
The laptop does not have a dedicated NVIDIA GPU, so processing was optimized to reduce CPU load.

- Target resolution: 640 × 360
- Target processing rate: 10 FPS
- Approximately every third frame was processed.

### Object Detection
The pretrained YOLO model detected general objects such as:

- Cars
- Buses
- Persons
- Other supported object classes

### Output
Output file:

`cv/inference/test_data/privacy_safe_output.mp4`

### Final Result

- Original frames read: 3601
- Frames processed: 1200
- Privacy-aware processing: Successful
- Object detection: Successful
- Output video generated: Successfully

### Key Achievement
A working privacy-aware Computer Vision video pipeline was implemented and tested locally.

---

# Current CV Progress

| Module | Status |
|---|---|
| CV-01 Environment Setup | Complete |
| CV-02 YOLO Baseline | Complete |
| CV-03 Reusable Detector | Complete |
| CV-04 Face Privacy | Complete |
| CV-05 Video Pipeline | Complete |
| CV-06 Road Defect Detection | Planned |

---

# Next Step

CV-06 will focus on project-specific road defect detection, beginning with pothole/road-damage dataset preparation and model training.