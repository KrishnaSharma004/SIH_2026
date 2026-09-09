from pathlib import Path
import random
import cv2


# ============================================================
# DATASET PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = (
    BASE_DIR
    / "datasets"
    / "bharatpothole"
    / "bharatpothole"
    / "BharatPotHole"
    / "BharatPotHole"
)

TRAIN_IMAGES = DATASET_DIR / "train" / "images"
TRAIN_LABELS = DATASET_DIR / "train" / "labels"

OUTPUT_DIR = BASE_DIR / "inspection_output"
OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# GET IMAGE FILES
# ============================================================

image_files = list(TRAIN_IMAGES.glob("*"))

print("========================================")
print("GROUND-TRUTH ANNOTATION INSPECTION")
print("========================================")

print(f"Training images: {len(image_files)}")
print(f"Training labels: {len(list(TRAIN_LABELS.glob('*.txt')))}")


# ============================================================
# RANDOM SAMPLE
# ============================================================

random.seed(42)

samples = random.sample(
    image_files,
    min(10, len(image_files))
)


# ============================================================
# DRAW YOLO GROUND-TRUTH BOXES
# ============================================================

for image_path in samples:

    image = cv2.imread(str(image_path))

    if image is None:
        print(f"Could not read: {image_path.name}")
        continue

    label_path = TRAIN_LABELS / f"{image_path.stem}.txt"

    if not label_path.exists():
        print(f"Label missing: {image_path.name}")
        continue

    height, width = image.shape[:2]

    with open(label_path, "r") as file:
        lines = file.readlines()

    for line in lines:

        values = line.strip().split()

        if len(values) != 5:
            continue

        class_id, x_center, y_center, box_width, box_height = map(
            float,
            values
        )

        # YOLO normalized coordinates
        x_center *= width
        y_center *= height
        box_width *= width
        box_height *= height

        # Convert center coordinates to corner coordinates
        x1 = int(x_center - box_width / 2)
        y1 = int(y_center - box_height / 2)

        x2 = int(x_center + box_width / 2)
        y2 = int(y_center + box_height / 2)

        # Draw bounding box
        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # Class name
        label = "pothole"

        cv2.putText(
            image,
            label,
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    output_path = OUTPUT_DIR / f"gt_{image_path.name}"

    cv2.imwrite(
        str(output_path),
        image
    )

    print(f"Saved: {output_path}")


print("========================================")
print("Ground-truth inspection completed.")
print(f"Output folder: {OUTPUT_DIR}")
print("========================================")