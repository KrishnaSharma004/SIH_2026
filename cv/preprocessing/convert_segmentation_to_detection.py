from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

DATASET_DIR = (
    BASE_DIR
    / "datasets"
    / "bharatpothole"
    / "bharatpothole"
    / "BharatPotHole"
    / "BharatPotHole"
)


def polygon_to_bbox(values):
    """
    Convert normalized YOLO polygon coordinates
    into normalized YOLO bounding-box format.

    Input:
        [x1, y1, x2, y2, ...]

    Output:
        [x_center, y_center, width, height]
    """

    xs = values[0::2]
    ys = values[1::2]

    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)

    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    width = x_max - x_min
    height = y_max - y_min

    return x_center, y_center, width, height


def convert_split(split):
    labels_dir = DATASET_DIR / split / "labels"

    converted_files = 0
    detection_rows = 0
    segmentation_rows = 0

    for label_file in labels_dir.glob("*.txt"):

        lines = label_file.read_text().splitlines()

        new_lines = []
        file_changed = False

        for line in lines:

            parts = line.strip().split()

            if not parts:
                continue

            class_id = parts[0]
            coordinates = list(map(float, parts[1:]))

            # YOLO detection format
            if len(parts) == 5:
                new_lines.append(line.strip())
                detection_rows += 1

            # YOLO segmentation format
            elif len(coordinates) >= 6 and len(coordinates) % 2 == 0:
                bbox = polygon_to_bbox(coordinates)

                new_line = (
                    f"{class_id} "
                    f"{bbox[0]:.10f} "
                    f"{bbox[1]:.10f} "
                    f"{bbox[2]:.10f} "
                    f"{bbox[3]:.10f}"
                )

                new_lines.append(new_line)

                segmentation_rows += 1
                file_changed = True

            else:
                print(f"WARNING: Unrecognized annotation: {label_file.name}")
                print(line)

        if file_changed:
            label_file.write_text("\n".join(new_lines) + "\n")
            converted_files += 1

    print(f"\n===== {split.upper()} =====")
    print(f"Files converted      : {converted_files}")
    print(f"Detection rows       : {detection_rows}")
    print(f"Segmentation rows    : {segmentation_rows}")


if __name__ == "__main__":

    print("Starting segmentation -> detection conversion...")

    convert_split("train")
    convert_split("valid")

    print("\n========================================")
    print("CONVERSION COMPLETED")
    print("========================================")