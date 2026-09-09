from pathlib import Path

from unified_detector import UnifiedCVDetector
from model_registry import ModelRegistry


BASE_DIR = Path(__file__).resolve().parents[1]


registry = ModelRegistry()

registry.register(
    "general_object_detector",
    BASE_DIR / "yolo11n.pt"
)

registry.register(
    "pothole_detector",
    BASE_DIR
    / "runs"
    / "pothole_yolo11n"
    / "weights"
    / "best.pt"
)


detector = UnifiedCVDetector(registry)


IMAGE_PATH = (
    Path(__file__).resolve().parent
    / "test_data"
    / "bus.jpg"
)


detections = detector.detect(
    IMAGE_PATH,
    confidence=0.35
)


print("\nUnified Detections")
print("==================")

for detection in detections:
    print(detection)