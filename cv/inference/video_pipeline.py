import cv2
from ultralytics import YOLO

from cv.privacy.face_blur import FaceBlur


class PrivacyAwareVideoPipeline:

    def __init__(
        self,
        object_model="yolo11n.pt",
        face_model="cv/models/yolov11n-face.pt"
    ):
        self.object_detector = YOLO(object_model)
        self.face_blur = FaceBlur(face_model)

    def process(
        self,
        input_path,
        output_path,
        target_width=640,
        target_fps=10
    ):

        cap = cv2.VideoCapture(input_path)

        if not cap.isOpened():
            raise FileNotFoundError(
                f"Unable to open video: {input_path}"
            )

        original_fps = cap.get(cv2.CAP_PROP_FPS)

        if original_fps <= 0:
            original_fps = 30

        original_width = int(
            cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        )

        original_height = int(
            cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

        # Keep aspect ratio while resizing
        scale = target_width / original_width

        target_height = int(
            original_height * scale
        )

        fourcc = cv2.VideoWriter_fourcc(
            *"mp4v"
        )

        writer = cv2.VideoWriter(
            output_path,
            fourcc,
            target_fps,
            (target_width, target_height)
        )

        frame_interval = max(
            1,
            round(original_fps / target_fps)
        )

        frame_count = 0
        processed_count = 0

        while True:

            success, frame = cap.read()

            if not success:
                break

            frame_count += 1

            # Process only selected frames
            if frame_count % frame_interval != 0:
                continue

            # Resize before AI processing
            frame = cv2.resize(
                frame,
                (target_width, target_height)
            )

            # Privacy first
            frame = self.face_blur.blur_faces(frame)

            # Object detection
            results = self.object_detector.predict(
                source=frame,
                conf=0.25,
                verbose=False
            )

            # Draw detections
            annotated_frame = results[0].plot()

            writer.write(annotated_frame)

            processed_count += 1

            if processed_count % 10 == 0:
                print(
                    f"Processed frames: {processed_count}"
                )

        cap.release()
        writer.release()

        print("\nProcessing complete.")
        print(f"Original frames read: {frame_count}")
        print(f"Frames processed: {processed_count}")
        print(f"Output saved to: {output_path}")


if __name__ == "__main__":

    input_video = (
        "cv/inference/test_data/test.ogv"
    )

    output_video = (
        "cv/inference/test_data/"
        "privacy_safe_output.mp4"
    )

    pipeline = PrivacyAwareVideoPipeline()

    pipeline.process(
        input_video,
        output_video,
        target_width=640,
        target_fps=10
    )