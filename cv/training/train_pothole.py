from pathlib import Path
from ultralytics import YOLO


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATASET_YAML = (
    BASE_DIR
    / "datasets"
    / "bharatpothole"
    / "bharatpothole"
    / "BharatPotHole"
    / "BharatPotHole"
    / "data.yaml"
)

MODEL_PATH = BASE_DIR / "yolo11n.pt"

RUNS_DIR = BASE_DIR / "runs"


# ============================================================
# LOAD PRETRAINED YOLO11n MODEL
# ============================================================

model = YOLO(str(MODEL_PATH))


# ============================================================
# TRAINING
# ============================================================

results = model.train(
    data=str(DATASET_YAML),
    epochs=1,
    imgsz=640,
    batch=8,
    device="cpu",
    workers=2,
    project=str(RUNS_DIR),
    name="pothole_yolo11n",
    exist_ok=True
)


# ============================================================
# TRAINING COMPLETE
# ============================================================

print("\n========================================")
print("POTHOLE MODEL TRAINING COMPLETED")
print("========================================")
print(f"Dataset: {DATASET_YAML}")
print(f"Results: {RUNS_DIR / 'pothole_yolo11n'}")
print(
    f"Best model: "
    f"{RUNS_DIR / 'pothole_yolo11n' / 'weights' / 'best.pt'}"
)
print("========================================")