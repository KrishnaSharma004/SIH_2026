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
- Segmentation mask when supported by the model

### Verified Test

The model was tested on an urban bus image through the unified CV inference pipeline.

Observed detections included:

- Bus — confidence: 0.9402
- Person — confidence: 0.8882
- Person — confidence: 0.8783
- Person — confidence: 0.8558
- Person — confidence: 0.6219

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

The framework is being used/planned for:

- Road-defect detection
- Vehicle detection
- Pedestrian detection
- Traffic-sign detection
- Model training
- Model validation
- Model inference
- Edge optimization

---

# 4. Pothole Detection Model

### Model

YOLO11n-based project-specific pothole detector.

### Purpose

Detect potholes as a project-specific road infrastructure defect.

### Dataset

BharatPotHole dataset.

### Dataset Statistics

- Training images: 5067
- Validation images: 1345
- Test images: 662
- Total images: 7074

### Dataset Class

Current pothole dataset contains:

- `pothole`

### Dataset Preparation

The dataset was inspected and ground-truth annotations were visually verified.

Some annotation files contained mixed detection and segmentation/polygon formats.

These annotations were converted into a consistent YOLO detection format using:

`cv/preprocessing/convert_segmentation_to_detection.py`

### Training

A YOLO11n training configuration was prepared in:

`cv/training/train_pothole.py`

Full training is planned on a suitable NVIDIA GPU system because CPU-based training on the development laptop was found to be too slow.

### Expected Model File

`cv/runs/pothole_yolo11n/weights/best.pt`

### Current Status

Dataset preparation: **Complete**

Annotation preprocessing: **Complete**

Training setup: **Complete**

Final trained model: **Pending**

---

# 5. Road Defect Detector

### File

`cv/inference/road_defect_detector.py`

### Purpose

Provide a reusable inference interface for project-specific road defects.

### Input

Image or video frame.

### Output

The detector returns:

- Defect type
- Class ID
- Confidence
- Bounding box

### Current Target

- Pothole

### Future Targets

The architecture can later support additional road-defect models.

### Current Status

Inference module implemented and ready for the trained pothole model.

---

# 6. Severity Estimation

### File

`cv/inference/severity.py`

### Purpose

Estimate the severity of a detected road defect.

### Inputs

- Detection confidence
- Bounding-box dimensions
- Frame dimensions

### Output

- Severity level
- Bounding-box area ratio

### Severity Levels

- Low
- Medium
- High

### Current Approach

Severity is currently estimated using a heuristic based on bounding-box area ratio and detection confidence.

### Limitation

This is an AI-estimated/heuristic value.

It does not represent physically measured pothole depth, width, or structural road damage.

### Current Status

Implemented and successfully tested.

---

# 7. Road Defect Event Generation

### File

`cv/inference/defect_event.py`

### Purpose

Convert a raw CV detection into a structured road-defect event.

### Event Fields

- Defect type
- Class ID
- Confidence
- Bounding box
- Severity
- Area ratio
- Latitude
- Longitude
- Timestamp

### Example

```text
defect_type: pothole
class_id: 0
confidence: 0.87
bbox: [320.5, 210.2, 480.7, 350.4]
severity: medium
area_ratio: 0.0108
latitude: 25.3176
longitude: 82.9739
timestamp: generated at runtime