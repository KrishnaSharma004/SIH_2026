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

# 2. Current CV Pipeline

Camera / Dashcam Video
        ↓
Frame Selection
        ↓
Frame Resize
        ↓
Face Detection
        ↓
Face Anonymization
        ↓
Object Detection
        ↓
Structured Detection Results
        ↓
Future: Road Defect Detection
        ↓
Future: GPS/Event Integration

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

---

# 4. Privacy by Design

A major requirement of the system is protecting personally identifiable visual information.

Faces detected in captured frames are blurred before the frame is used for further processing or persistent storage.

This creates a privacy-aware processing pipeline.

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

# 6. Demonstrated Result

The complete video pipeline was successfully tested.

### Test Result

- Original frames read: 3601
- Frames processed: 1200
- Face anonymization: Successful
- Object detection: Successful
- Output video: Successfully generated

### Output

`privacy_safe_output.mp4`

---

# 7. Current Detection Capability

The pretrained YOLO model currently detects general objects such as:

- Cars
- Buses
- Persons
- Other supported general classes

This is a baseline capability.

---

# 8. Project-Specific CV

The final system requires specialized models for urban infrastructure intelligence.

Planned detection tasks:

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

# 9. Innovation — Repeated Sightings

A detected road defect can be observed by multiple buses.

Instead of treating every detection as a separate problem:

Bus A
→ Pothole detected
→ GPS location

Bus B
→ Same pothole detected
→ Similar GPS location

Bus C
→ Same pothole detected
→ Similar GPS location

The backend can combine these observations into one road issue with increased confidence.

This supports reliable urban infrastructure reporting.

---

# 10. SIH Presentation Points

### Problem
Manual road-condition monitoring is slow, expensive and difficult to scale.

### Solution
Use public transport vehicles as mobile AI-powered sensing units.

### CV Contribution
Process bus/dashcam video to detect road, traffic and infrastructure-related objects/events.

### Privacy
Faces are detected and blurred before further processing.

### Scalability
The same architecture can process video from multiple buses.

### Future Edge Deployment
The trained models can later be optimized using techniques such as INT8 quantization and TensorRT for deployment on edge hardware such as NVIDIA Jetson.

---

# 11. Challenges and Solutions

| Challenge | Solution |
|---|---|
| CPU-only development machine | Reduced processing resolution and FPS |
| OpenCV face detection approach unavailable in current environment | Used dedicated YOLO face model |
| Python package import issue | Added package initialization files and used module execution |
| General YOLO model does not detect potholes | Plan project-specific model training |
| Privacy of captured faces | Face detection + Gaussian blur |

---

# 12. Current Progress

| Component | Status |
|---|---|
| CV Environment | Complete |
| YOLO Baseline | Complete |
| Reusable Detector | Complete |
| Face Detection | Complete |
| Face Anonymization | Complete |
| Video Pipeline | Complete |
| Pothole Detection | Next |
| Road Damage Detection | Planned |
| Waterlogging Detection | Planned |
| Traffic Sign Detection | Planned |
| Edge Optimization | Planned |

---

# 13. One-Line Presentation Explanation

"Hum public buses ko mobile AI sensing units ki tarah use kar rahe hain, jahan onboard Computer Vision video ko process karke road aur traffic conditions ko automatically detect karta hai, while maintaining privacy through face anonymization."

---

# 14. Next Development Step

CV-06:

Road-defect dataset preparation and pothole detection model development.