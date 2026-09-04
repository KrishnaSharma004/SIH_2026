from ultralytics import YOLO
import cv2


class FaceBlur:
    def __init__(self, model_path="cv/models/yolov11n-face.pt"):
        self.model = YOLO(model_path)

    def blur_faces(self, frame, confidence=0.25):
        results = self.model.predict(
            source=frame,
            conf=confidence,
            verbose=False
        )

        for result in results:
            if result.boxes is None:
                continue

            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()

                x1, y1, x2, y2 = map(
                    int,
                    [x1, y1, x2, y2]
                )

                x1 = max(0, x1)
                y1 = max(0, y1)
                x2 = min(frame.shape[1], x2)
                y2 = min(frame.shape[0], y2)

                face = frame[y1:y2, x1:x2]

                if face.size == 0:
                    continue

                blurred_face = cv2.GaussianBlur(
                    face,
                    (51, 51),
                    30
                )

                frame[y1:y2, x1:x2] = blurred_face

        return frame


if __name__ == "__main__":
    image_path = "bus.jpg"
    output_path = "cv/privacy/blurred_test.jpg"

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    face_blur = FaceBlur()

    blurred_image = face_blur.blur_faces(image)

    cv2.imwrite(output_path, blurred_image)

    print(
        f"Privacy-safe image saved to: {output_path}"
    )