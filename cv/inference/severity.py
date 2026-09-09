def estimate_severity(detection, frame_width, frame_height):
    """
    Estimate pothole severity using bounding-box area
    and detection confidence.
    """

    x1, y1, x2, y2 = detection["bbox"]

    bbox_width = max(0, x2 - x1)
    bbox_height = max(0, y2 - y1)

    bbox_area = bbox_width * bbox_height
    frame_area = frame_width * frame_height

    area_ratio = bbox_area / frame_area if frame_area > 0 else 0

    confidence = detection["confidence"]

    if area_ratio >= 0.15 or confidence >= 0.90:
        severity = "high"

    elif area_ratio >= 0.05 or confidence >= 0.70:
        severity = "medium"

    else:
        severity = "low"

    return {
        "severity": severity,
        "area_ratio": round(area_ratio, 4)
    }


if __name__ == "__main__":

    sample_detection = {
        "defect_type": "pothole",
        "confidence": 0.87,
        "bbox": [320.5, 210.2, 480.7, 350.4]
    }

    result = estimate_severity(
        sample_detection,
        frame_width=1920,
        frame_height=1080
    )

    print(result)