# Computer Vision — SIH PPT Notes

## Project

AI-Powered Mobile Urban Intelligence Platform Using Public Transport Fleet

## Developer

Vansh

---

# 1. Computer Vision Role

Public transport buses are treated as mobile sensing units.

Their camera/video feeds can be processed to identify road and traffic-related events.

The Computer Vision layer is responsible for converting visual data into structured detections that can later become georeferenced urban intelligence events.

---

# 2. Current CV Architecture

Camera / Dashcam Video

        ↓

Privacy Processing

        ↓

Frame / Image

        ↓

Model Registry

        ↓

Unified CV Detector

        ↓

Multiple CV Models

        ↓

Result Parser

        ↓

Unified Detection Results

        ↓

Defect Event Generation

        ↓

JSON Serialization

        ↓

Future: Backend / GPS Integration

---

# 3. Technology Used

### Programming

- Python

### Computer Vision

- OpenCV

### AI / Object Detection

- Ultralytics YOLO

### Deep Learning Framework

- PyTorch

### Models

- YOLO11n
- YOLO11n Face Detection Model
- YOLO11n-based Pothole Model — training pending

---

# 4. Privacy by Design

A major requirement of the system is protecting personally identifiable visual information.

Faces detected in captured frames are blurred before the frame is used for further processing or persistent storage.

### Privacy Flow

Raw Frame

→ Face Detection

→ Face Blur

→ Privacy-Safe Frame

→ Further CV Processing

---

# 5. CPU Optimization

Initial development is being performed on a CPU-only laptop.

To reduce computational load:

- Input resolution: 1920 × 1080
- Processing resolution: 640 × 360
- Original video: 30 FPS
- Processing target: 10 FPS
- Approximately every third frame is processed

This allows the pipeline to be tested locally without requiring a dedicated GPU.

---

# 6. Demonstrated Video Pipeline Result

The complete privacy-aware video pipeline was successfully tested.

### Test Result

- Original frames read: 3601
- Frames processed: 1200
- Face anonymization: Successful
- Object detection: Successful
- Output video: Successfully generated

### Output

`privacy_safe_output.mp4`

---

# 7. General Object Detection

The pretrained YOLO11n model currently detects general objects such as:

- Cars
- Buses
- Persons
- Other supported general classes

### Example Unified Detection

A test urban bus image produced structured detections including:

- Bus — confidence: 0.9402
- Person — confidence: 0.8882
- Person — confidence: 0.8783
- Person — confidence: 0.8558
- Person — confidence: 0.6219

This confirms that the unified inference architecture is working successfully.

---

# 8. Project-Specific CV

The final system requires specialized models for urban infrastructure intelligence.

### Current Project-Specific Target

- Pothole detection

### Planned Detection Tasks

- Pothole detection
- Road crack/damage detection
- Waterlogging detection
- Missing divider detection
- Missing zebra-crossing detection
- Traffic-sign detection
- Vehicle detection/classification
- Pedestrian detection

These models will be trained or fine-tuned using appropriate datasets.

---

# 9. Pothole Detection Development

The BharatPotHole dataset has been prepared for project-specific pothole detection.

### Dataset

- Training images: 5067
- Validation images: 1345
- Test images: 662
- Total images: 7074

### Dataset Preparation

Ground-truth annotations were visually verified.

Some label files contained mixed detection and segmentation annotations.

These were converted into a consistent YOLO detection format.

### Preprocessing Result

- Training problematic files: 116 → 0
- Validation problematic files: 29 → 0

### Current Status

Dataset preparation: Complete

Annotation preprocessing: Complete

Training setup: Complete

Full model training: Pending on GPU

---

# 10. Modular Multi-Model Architecture

Instead of depending on a single model for every task, the system uses a modular architecture.

### Model Registry

The registry maintains available CV models.

Current registered models:

- `general_object_detector`
- `pothole_detector`

If a model file is unavailable, the system can safely skip it until the model becomes available.

### Unified Detector

All available models can be accessed through:

`UnifiedCVDetector`

### Architecture

Model Registry

→ Unified CV Detector

→ Individual CV Models

→ Result Parser

→ Unified Detection Output

This allows future CV models to be added without redesigning the complete inference pipeline.

---

# 11. Unified Detection Output

Different CV models are converted into a common structured format.

### Output Fields

- Model
- Class ID
- Class name
- Confidence
- Bounding box
- Mask, when available

### Example

```text
{
    "model": "general_object_detector",
    "class_id": 5,
    "class_name": "bus",
    "confidence": 0.9402,
    "bbox": [3.83, 229.36, 796.19, 728.41],
    "mask": None
}