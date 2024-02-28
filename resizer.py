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

    # determine new image's dimensions
    long_side = max(original_image.width, original_image.height)
    short_side = min(original_image.width, original_image.height)

    if format == "square":
        zoomed_size = (long_side, long_side)
    elif format == "portrait":  # 4:5 ratio
        r = long_side // 5
        zoomed_size = (r * 4, r * 5)
    else:
        zoomed_size = (original_image.width, original_image.height)

    # set up "background" layer
    if background == "black":
        result_image = Image.new(mode="RGB", size=zoomed_size, color="black")
    elif background == "blur":
        result_image = original_image.resize(size=zoomed_size)
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

    # crop out if needed
    if format == "portrait":  # 4:5 portrait for instagram
        width_to_crop = result_image.width / 10
        width_crop_box = (width_to_crop, 0, result_image.width - width_to_crop, result_image.height)
        result_image = result_image.crop(width_crop_box)

    result_image.save(fp=f"{filename}_edit.{extension}", quality=100, exif=exif_data, icc_profile=bytes(icc_profile))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('images', metavar='I', nargs='+', type=str, help='path to images')
    # parser.add_argument('format', metavar='F', action='store', help='format, default is square', default='square')
    # parser.add_argument('background', metavar='B', action='store', help='background color, default is blur', default='blur')
    args = parser.parse_args()

    for image_path in args.images:
        if os.path.isdir(image_path):
            for image_filename in os.listdir(image_path):
                if '_edit.' in image_filename:
                    continue
                elif image_filename.endswith('.jpg') or image_filename.endswith('.png'):
                    blur_background(os.path.join(image_path, image_filename))
        elif os.path.isfile(image_path):
            blur_background(image_path)
