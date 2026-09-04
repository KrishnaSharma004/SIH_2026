from ultralytics import YOLO


class VideoDetector:
    def __init__(self, model_path="yolo11n.pt"):
        self.model = YOLO(model_path)

    def process_video(self, source, output_path="runs/video_detection"):
        results = self.model.predict(
            source=source,
            conf=0.25,
            save=True,
            project=output_path,
            name="result",
            verbose=False
        )

        return results


if __name__ == "__main__":
    detector = VideoDetector()

    detector.process_video(
        "cv/inference/test_data/test.mp4"
    )