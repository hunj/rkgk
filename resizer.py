import os
from PIL import Image, ImageFilter
import argparse


def blur_background(image_path, format="square", background="blur", blur_radius=32):
    # some setup
    print(image_path)
    filename = "".join(image_path.split('.')[:-1])
    extension = image_path.split('.')[-1]

    # load shit up
    original_image = Image.open(image_path)
    icc_profile = original_image.info.get('icc_profile')
    exif_data = original_image.info.get('exif')
    ratio = original_image.height / original_image.width

    save_info = {
        "fp": f"{filename}_edit.{extension}",
        "quality": 100,
        "exif": exif_data,
    }

    if icc_profile:
        save_info["icc_profile"] = icc_profile

    # determine new image's dimensions
    long_side = max(original_image.width, original_image.height)
    if format == "square":
        background_size = (long_side, long_side)
    elif format == "portrait":  # 4:5 ratio for instagram
        r = long_side // 5
        background_size = (r * 4, r * 5)
    else:
        background_size = (original_image.width, original_image.height)

    # set up "background" layer
    if background == "black":
        result_image = Image.new(mode="RGB", size=background_size, color="black")
    elif background == "blur":
        result_image = original_image.resize(size=background_size)
        result_image = result_image.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    # paste the original image on top of the bg layer
    paste_box = (0, 0)  # left, top offset
    if ratio < 1:  # landscape photo
        crop_point = round((result_image.height - original_image.height) / 2)
        paste_box = (0, crop_point)
    else:  # portrait photo
        crop_point = round((result_image.width - original_image.width) / 2)
        paste_box = (crop_point, 0)

    result_image.paste(original_image, box=paste_box)

    result_image.save(**save_info)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('images', metavar='I', nargs='+', type=str, help='path to images')
    parser.add_argument('-b', '--black', action='store_true')
    parser.add_argument('-s', '--square', action='store_true', help='format, default is square')
    parser.add_argument('-r', '--radius', type=int, default=32)
    args = parser.parse_args()

    format = "square" if args.square else "portrait"
    background = "black" if args.black else "blur"

    for image_path in args.images:
        if os.path.isdir(image_path):
            for image_filename in os.listdir(image_path):
                if '_edit.' in image_filename:
                    continue
                elif image_filename.endswith('.jpg') or image_filename.endswith('.png'):
                    blur_background(
                        os.path.join(image_path, image_filename),
                        format=format,
                        background=background,
                        blur_radius=args.radius,
                    )
        elif os.path.isfile(image_path):
            blur_background(
                image_path,
                format=format,
                background=background,
                blur_radius=args.radius,
            )
