from pathlib import Path


class ModelRegistry:
    """
    Stores all CV models used by the unified detector.
    """

    def __init__(self):
        self.models = {}

    def register(self, name, model_path):
        model_path = Path(model_path)

        self.models[name] = {
            "path": str(model_path),
            "exists": model_path.exists()
        }

    def get_models(self):
        return self.models


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

    print("\nRegistered CV Models")
    print("===================")

    for name, info in registry.get_models().items():
        print(f"{name}:")
        print(f"  path   : {info['path']}")
        print(f"  exists : {info['exists']}")