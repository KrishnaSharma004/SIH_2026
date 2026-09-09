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

# CV-06 — Road Defect Dataset Preparation

### Objective

Prepare a project-specific road defect dataset for training a pothole detection model.

### Dataset

BharatPotHole dataset was used for pothole detection.

### Dataset Structure

The dataset contains:

- `train`
- `valid`
- `test`
- `data.yaml`

### Dataset Statistics

- Training images: 5067
- Validation images: 1345
- Test images: 662
- Total images: 7074

Corresponding YOLO label files were available for the dataset splits.

### Dataset Verification

Ground-truth annotations were visually inspected using sample images.

The pothole bounding-box annotations were verified to be correctly aligned with the road defects.

### Annotation Issue Found

Some label files contained mixed YOLO annotation formats.

A number of files contained segmentation/polygon rows instead of standard detection rows.

Problematic files found:

- Training split: 116 files
- Validation split: 29 files

### Backup

Before modifying the labels, backups were created for:

`train/labels`

`valid/labels`

### Preprocessing

A preprocessing script was created:

`cv/preprocessing/convert_segmentation_to_detection.py`

The script converts normalized YOLO polygon coordinates into bounding-box detection coordinates.

### Conversion Result

Training split:

- 116 files converted
- 8519 existing detection rows
- 276 segmentation rows converted

Validation split:

- 29 files converted
- 2210 existing detection rows
- 66 segmentation rows converted

### Verification

After preprocessing:

- Training problematic files: 0
- Validation problematic files: 0

The dataset was successfully converted into a consistent detection format.

### Model Training Status

A YOLO11n pothole training setup was prepared using:

`cv/training/train_pothole.py`

The training configuration uses:

- Model: YOLO11n
- Image size: 640
- Batch size: 8
- Device: CPU during local testing

Local CPU training was found to be too slow for full training.

### Current Training Plan

Full pothole model training will be performed on a system with a suitable NVIDIA GPU.

The trained model is expected at:

`cv/runs/pothole_yolo11n/weights/best.pt`

### Current Status

Dataset preparation and preprocessing: **Complete**

Model training: **Pending / Outsourced to GPU system**

---

# CV-07 — Road Defect Detection Module

### Objective

Create a reusable inference module specifically for project-specific road defects.

### File Created

`cv/inference/road_defect_detector.py`

### Work Done

- Created `RoadDefectDetector` class.
- Added configurable model path.
- Added configurable confidence threshold.
- Added YOLO model loading.
- Added detection inference.
- Converted detections into structured road-defect information.

### Detection Output

Each detected road defect returns:

- Defect type
- Class ID
- Confidence
- Bounding box

### Expected Defect

Current dataset/model target:

- Pothole

Future project-specific defect models can be added later.

### Model Dependency

The detector is prepared to use:

`cv/runs/pothole_yolo11n/weights/best.pt`

The model file is currently not present because full training is pending.

### Result

The road defect inference module has been implemented and is ready for the trained pothole model.

---

# CV-08 — Road Defect Severity Estimation

### Objective

Generate an estimated severity level for detected road defects.

### File Created

`cv/inference/severity.py`

### Work Done

A heuristic severity estimation method was implemented using:

- Bounding-box area relative to frame area
- Detection confidence

### Severity Levels

- Low
- Medium
- High

### Output

The module returns:

- Severity
- Bounding-box area ratio

### Important Limitation

The current severity estimation is a heuristic and does not represent physically measured pothole depth, width, or actual road damage severity.

It should therefore be treated as an AI-estimated/heuristic severity value until a better severity-labelled dataset or physical measurement method is available.

### Result

Severity estimation logic was successfully implemented and tested.

---

# CV-09 — Road Defect Event Generation

### Objective

Convert raw CV detections into complete road-defect events that can later be consumed by the backend/API.

### File Created

`cv/inference/defect_event.py`

### Work Done

The module combines:

- Defect type
- Class ID
- Confidence
- Bounding box
- Severity
- Area ratio
- Latitude
- Longitude
- Timestamp

### Example Event

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