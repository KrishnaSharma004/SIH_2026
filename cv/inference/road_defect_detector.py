from pathlib import Path

from ultralytics import YOLO


class RoadDefectDetector:
    def __init__(self, model_path, confidence=0.35):
        self.model_path = Path(model_path)
        self.confidence = confidence

        self.model = YOLO(str(self.model_path))

    def detect(self, source):
        results = self.model.predict(
            source=source,
            conf=self.confidence,
            verbose=False
        )

        detections = []

        for result in results:
            names = result.names

            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence_score = float(box.conf[0])

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                detections.append({
                    "defect_type": names[class_id],
                    "class_id": class_id,
                    "confidence": round(confidence_score, 4),
                    "bbox": [
                        round(x1, 2),
                        round(y1, 2),
                        round(x2, 2),
                        round(y2, 2)
                    ]
                })

        return detections


if __name__ == "__main__":

    MODEL_PATH = (
        Path(__file__).resolve().parents[1]
        / "runs"
        / "pothole_yolo11n"
        / "weights"
        / "best.pt"
    )

    detector = RoadDefectDetector(MODEL_PATH)

    print("Road defect detector ready.")
    print(f"Model: {MODEL_PATH}")