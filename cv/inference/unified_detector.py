from pathlib import Path

from ultralytics import YOLO

from result_parser import parse_result
from model_registry import ModelRegistry


class UnifiedCVDetector:
    """
    Central CV inference interface.

    Loads CV models from the model registry
    and returns unified detections.
    """

    def __init__(self, registry):
        self.registry = registry
        self.models = {}

        self._load_models()

    def _load_models(self):
        """
        Load all available models from the registry.
        """

        for model_name, info in self.registry.get_models().items():

            if not info["exists"]:
                print(
                    f"Skipping {model_name}: "
                    f"model file not found."
                )
                continue

            self.models[model_name] = YOLO(info["path"])

    def detect(self, source, confidence=0.35):
        """
        Run all loaded models on the input source.
        """

        detections = []

        for model_name, model in self.models.items():

            results = model.predict(
                source=source,
                conf=confidence,
                verbose=False
            )

            for result in results:

                parsed_detections = parse_result(
                    result,
                    model_name
                )

                detections.extend(parsed_detections)

        return detections


if __name__ == "__main__":

    registry = ModelRegistry()

    registry.register(
        "general_object_detector",
        Path(__file__).resolve().parents[1] / "yolo11n.pt"
    )

    registry.register(
        "pothole_detector",
        Path(__file__).resolve().parents[1]
        / "runs"
        / "pothole_yolo11n"
        / "weights"
        / "best.pt"
    )

    detector = UnifiedCVDetector(registry)

    print("\nUnified CV Detector")
    print("===================")
    print(
        f"Loaded models: "
        f"{list(detector.models.keys())}"
    )