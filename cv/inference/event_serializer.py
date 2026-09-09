import json


def serialize_event(event):
    """
    Convert a road-defect event dictionary
    into an API-ready JSON payload.
    """

    return json.dumps(
        event,
        indent=4
    )


if __name__ == "__main__":

    sample_event = {
        "defect_type": "pothole",
        "class_id": 0,
        "confidence": 0.87,
        "bbox": [320.5, 210.2, 480.7, 350.4],
        "severity": "medium",
        "area_ratio": 0.0108,
        "latitude": 25.3176,
        "longitude": 82.9739,
        "timestamp": "2026-09-09T15:57:33.290717"
    }

    json_payload = serialize_event(sample_event)

    print("\nAPI-Ready JSON")
    print("=================")
    print(json_payload)