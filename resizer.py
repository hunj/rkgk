from PIL import Image, ImageFilter
import argparse


def square_img(image_path):
    filename = "".join(image_path.split('.')[:-1])
    extension = image_path.split('.')[-1]

    original_image = Image.open(image_path)
    exif_data = original_image.info.get('exif')
    ratio = original_image.height / original_image.width

    result_image = original_image.copy()
    result_image = result_image.rotate(90) if ratio < 1 else result_image

    zoomed_size = (round(original_image.width * ratio), round(original_image.height * ratio))
    result_image = original_image.resize(size=zoomed_size)
    length_to_crop = round((result_image.height - original_image.height) / 2)

    crop_box = (0, length_to_crop, result_image.width, result_image.height - length_to_crop)
    result_image = result_image.crop(crop_box).filter(ImageFilter.GaussianBlur(radius=round(original_image.height / (ratio * 100))))

    result_image.paste(original_image, (round((original_image.height - original_image.width) / 2 ), 0))

    result_image = result_image.rotate(-90) if ratio < 1 else result_image
    result_image.save(fp=f"{filename}_edit.{extension}", quality=100, exif=exif_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('images',
            metavar='I',
            nargs='+',
            type=str, help='path to images')
    args = parser.parse_args()

    for image_path in args.images:
        if image_path[1] == ":":
            image_path = "/mnt/{drive}/{path}".format(
                    drive=image_path[0].lower(),
                    path="/".join(image_path.split("\\")[1:])
            )
        print(image_path)
        square_img(image_path)
