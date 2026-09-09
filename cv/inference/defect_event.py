from datetime import datetime

from severity import estimate_severity


def create_defect_event(
    detection,
    frame_width,
    frame_height,
    latitude=None,
    longitude=None
):
    """
    Convert a raw CV detection into a complete road-defect event.
    """

    severity_result = estimate_severity(
        detection,
        frame_width,
        frame_height
    )

    event = {
        "defect_type": detection["defect_type"],
        "class_id": detection["class_id"],
        "confidence": detection["confidence"],
        "bbox": detection["bbox"],
        "severity": severity_result["severity"],
        "area_ratio": severity_result["area_ratio"],
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": datetime.now().isoformat()
    }

    return event


if __name__ == "__main__":

    sample_detection = {
        "defect_type": "pothole",
        "class_id": 0,
        "confidence": 0.87,
        "bbox": [320.5, 210.2, 480.7, 350.4]
    }

    event = create_defect_event(
        detection=sample_detection,
        frame_width=1920,
        frame_height=1080,
        latitude=25.3176,
        longitude=82.9739
    )

    print("\nRoad Defect Event")
    print("=================")

    for key, value in event.items():
        print(f"{key}: {value}")