from ultralytics import YOLO


class CVDetector:
    def __init__(self, model_path="yolo11n.pt"):
        self.model = YOLO(model_path)

    def detect(self, source, confidence=0.25):
        results = self.model.predict(
            source=source,
            conf=confidence,
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
                    "class_id": class_id,
                    "class_name": names[class_id],
                    "confidence": confidence_score,
                    "bbox": [
                        round(x1, 2),
                        round(y1, 2),
                        round(x2, 2),
                        round(y2, 2)
                    ]
                })

        return detections


if __name__ == "__main__":
    detector = CVDetector()

    detections = detector.detect(
        "bus.jpg"
    )

    for detection in detections:
        print(detection)