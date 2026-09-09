# CV-06 — Pothole Detection

## Objective

Develop a project-specific Computer Vision model for detecting potholes and road defects.

## Dataset

BharatPotHole dataset

## Dataset Statistics

- Training images: 5067
- Validation images: 1345
- Test images: 662
- Total images: 7074

## Dataset Structure

The dataset contains:

- `train/images`
- `train/labels`
- `valid/images`
- `valid/labels`
- `test/images`
- `test/labels`
- `data.yaml`

The dataset contains a single project-specific detection class:

- `pothole`

## Dataset Verification

Ground-truth annotations were visually inspected using randomly selected samples.

The pothole bounding-box annotations were verified to be correctly aligned with the road defects.

## Annotation Issue Found

During dataset verification, some label files were found to contain mixed YOLO annotation formats.

Some files contained polygon/segmentation annotations instead of standard YOLO detection bounding-box annotations.

Problematic files:

- Training: 116
- Validation: 29

## Annotation Backup

Before modifying the annotations, backups were created for:

- `train/labels`
- `valid/labels`

## Preprocessing

A conversion script was created:

`cv/preprocessing/convert_segmentation_to_detection.py`

The script converts normalized YOLO polygon coordinates into normalized bounding-box coordinates.

### Conversion Results

Training:

- 116 files converted
- 8519 existing detection rows
- 276 segmentation rows converted

Validation:

- 29 files converted
- 2210 existing detection rows
- 66 segmentation rows converted

## Post-Processing Verification

After conversion:

- Training problematic files: 0
- Validation problematic files: 0

The training and validation annotations were successfully converted into a consistent YOLO detection format.

## Training Setup

A YOLO11n training script was prepared:

`cv/training/train_pothole.py`

### Configuration

- Model: YOLO11n
- Image size: 640
- Batch size: 8
- Training device: CPU for local testing

## Training Observation

A local CPU training test was started, but full training on the laptop was found to be too slow.

Therefore, full model training will be performed on a suitable NVIDIA GPU system.

## Model Output

The expected trained model is:

`cv/runs/pothole_yolo11n/weights/best.pt`

Current status:

`best.pt` is not yet available.

## Road Defect Detector

A reusable road defect inference module was created:

`cv/inference/road_defect_detector.py`

The module is designed to load the trained pothole model and return:

- Defect type
- Class ID
- Confidence
- Bounding box

## Severity Estimation

A heuristic severity estimation module was created:

`cv/inference/severity.py`

Severity is estimated using:

- Bounding-box area relative to frame area
- Detection confidence

Possible severity levels:

- Low
- Medium
- High

The current severity system is heuristic and should not be considered a physical measurement of pothole severity.

## Defect Event Generation

A road-defect event module was created:

`cv/inference/defect_event.py`

The event structure contains:

- Defect type
- Class ID
- Confidence
- Bounding box
- Severity
- Area ratio
- Latitude
- Longitude
- Timestamp

## Event Serialization

An API-ready JSON serialization module was created:

`cv/inference/event_serializer.py`

This converts structured road-defect events into JSON payloads for future backend/API integration.

## Status

### Completed

- Dataset downloaded
- Dataset structure verified
- Ground-truth annotations visually verified
- Annotation inconsistencies identified
- Label backups created
- Segmentation-to-detection conversion completed
- Post-processing verification completed
- YOLO11n training setup prepared
- Road defect detector module created
- Severity estimation module created
- Defect event generation created
- JSON event serialization created

### Pending

- Full pothole model training on GPU
- Validation and evaluation of trained model
- Model optimization
- Integration of trained `best.pt`

## Results

Dataset preparation and preprocessing: **Successful**

Road defect inference architecture: **Implemented**

Pothole model training: **Pending on GPU**

Final detection metrics: **Pending**