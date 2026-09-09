def parse_result(result, model_name):
    """
    Convert an Ultralytics result into a unified format.

    Supports:
    - Bounding-box detections
    - Segmentation masks
    """

    detections = []

    names = result.names

    # -----------------------------
    # Bounding-box detections
    # -----------------------------
    if result.boxes is not None:

        for index, box in enumerate(result.boxes):

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            detection = {
                "model": model_name,
                "class_id": class_id,
                "class_name": names[class_id],
                "confidence": round(confidence, 4),
                "bbox": [
                    round(x1, 2),
                    round(y1, 2),
                    round(x2, 2),
                    round(y2, 2)
                ]
            }

            # -----------------------------
            # Segmentation mask
            # -----------------------------
            if result.masks is not None:

                mask = result.masks.data[index]

                detection["mask"] = mask.cpu().numpy().tolist()

            else:
                detection["mask"] = None

            detections.append(detection)

    return detections


if __name__ == "__main__":
    print("Result parser ready.")
    print("Supports bounding boxes and segmentation masks.")