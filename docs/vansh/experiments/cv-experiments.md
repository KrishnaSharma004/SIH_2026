# Computer Vision Experiments

## Project
AI-Powered Mobile Urban Intelligence Platform Using Public Transport Fleet

## Developer
Vansh

---

# Experiment 01 — YOLO11n Baseline Image Detection

### Objective
Test whether the pretrained YOLO11n model can successfully perform object detection on the development machine.

### Input
Sample urban/bus image.

### Model
YOLO11n pretrained model.

### Hardware
- CPU: AMD Ryzen 5 5500U
- GPU: Not available

### Observed Detection
The model successfully detected:

- Bus
- Persons

### Result
Baseline object detection was successful.

### Conclusion
The pretrained model is suitable for establishing the initial Computer Vision pipeline.

---

# Experiment 02 — Face Detection and Anonymization

### Objective
Verify that faces can be detected and anonymized before visual data is used further.

### Model
YOLO11n face detection model.

### Input
Sample image containing people.

### Processing
Face Detection
→ Face Bounding Box
→ Gaussian Blur

### Result
Faces were successfully detected and blurred.

### Conclusion
The privacy-anonymization component works successfully.

---

# Experiment 03 — Privacy-Aware Video Pipeline

### Objective
Test the complete video-processing pipeline on an urban dashcam video while keeping CPU usage manageable.

### Input Video

- Resolution: 1920 × 1080
- Original FPS: 30
- Original frames read: 3601

### Optimization

Because development was performed on a CPU-only laptop, the input was optimized before AI processing.

- Target width: 640 pixels
- Target height: 360 pixels
- Target FPS: 10
- Frame interval: approximately every 3rd frame

### Processing Pipeline

Video
→ Frame Selection
→ Resize
→ Face Detection
→ Face Blur
→ YOLO Object Detection
→ Annotated Video Output

### Result

- Original frames read: 3601
- Frames processed: 1200
- Output generated successfully
- Face anonymization worked
- General object detection worked

### Output

`cv/inference/test_data/privacy_safe_output.mp4`

### Observation

The model successfully marked general road-scene objects such as cars, buses and persons.

### Performance Observation

CPU processing generated moderate laptop heat, but the pipeline continued processing successfully.

### Conclusion

The optimized pipeline is suitable for local functional testing. Further optimization and model acceleration will be required for real-time edge deployment.

---

# Experiment 04 — General Object Detection vs Project-Specific Detection

### Observation

The pretrained YOLO11n model detects general object classes.

It does not directly provide the project's required road-infrastructure classes such as:

- Potholes
- Road cracks
- Waterlogging
- Missing dividers
- Missing zebra crossings

### Conclusion

A project-specific dataset and trained/fine-tuned model are required.

This experiment establishes the need for the next Computer Vision stage:

Dataset Preparation
→ Annotation Verification
→ Model Training
→ Evaluation

---

# Current Experimental Summary

| Experiment | Result |
|---|---|
| YOLO11n baseline detection | Successful |
| Face detection | Successful |
| Face anonymization | Successful |
| Video processing | Successful |
| CPU optimization | Successful |
| Project-specific defect detection | Planned |

---

# Next Experiment

CV-06 will begin with road-defect dataset preparation and pothole detection model development.