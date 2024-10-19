import os
import time
from PIL import Image
from datetime import datetime


INPUT_DIR_PATH = "/Users/hunj/Pictures/Capture One Catalog.cocatalog/Originals/"
OUTPUT_DIR_PATH = "/Users/hunj/Library/CloudStorage/GoogleDrive-iroun.photos@gmail.com/My Drive/Tekko 2024 Halloween Spooktacular/"
OVERLAY_IMG_PATH = "/Users/hunj/Desktop/tekko/overlay.png"

INTERVAL_SECONDS = 5.0
RESCALE_WIDTH = 1600


OVERLAY = Image.open(OVERLAY_IMG_PATH).convert("RGBA")

def add_overlay(image_path, destination=OUTPUT_DIR_PATH):
    base_image = Image.open(os.path.join(image_path))
    filename = image_path.split('/')[-1]
    icc_profile = base_image.info.get('icc_profile')
    exif_data = base_image.info.get('exif')

    dest = os.path.join(destination + filename)

    save_info = {
        "fp": dest,
        "quality": 100,
        "exif": exif_data,
    }

    if icc_profile:
        save_info["icc_profile"] = icc_profile

    base_image.paste(OVERLAY, (0, 0), OVERLAY)
    base_image.resize((base_image.width // 2, base_image.height // 2))
    base_image.save(**save_info)


def scan_for_images():
    inputs = [os.path.join(dp, f) for dp, _, fn in os.walk(os.path.expanduser(INPUT_DIR_PATH)) for f in fn]
    outputs = list(map(lambda p: p.split('/')[-1], os.listdir(OUTPUT_DIR_PATH)))
    return [filename for filename in inputs if filename.split('/')[-1] not in outputs and filename.endswith(".JPG")]


if __name__ == '__main__':
    while True:
        now = datetime.now().astimezone().replace(microsecond=0).isoformat
        to_process = scan_for_images()
        if to_process:
            print(f"[{now()}] Processing {len(to_process)} files...")
            for img_filepath in to_process:
                add_overlay(os.path.join(img_filepath))
                print(f"[{now()}] Processed {img_filepath}")

        time.sleep(INTERVAL_SECONDS)
