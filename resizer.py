from PIL import Image, ImageFilter

IMAGE_PATH = "DEEZ_NUTS.jpg"

filename = "".join(IMAGE_PATH.split('.')[:-1])
extension = IMAGE_PATH.split('.')[-1]

original_image = Image.open(IMAGE_PATH)
ratio = original_image.height / original_image.width

result_image = original_image.copy()

zoomed_size = (round(original_image.width * ratio), round(original_image.height * ratio))
result_image = original_image.resize(size=zoomed_size)
length_to_crop = round((result_image.height - original_image.height) / 2)

crop_box = (0, length_to_crop, result_image.width, result_image.height - length_to_crop)
result_image = result_image.crop(crop_box).filter(ImageFilter.GaussianBlur(radius=round(original_image.height / (ratio * 100))))

result_image.paste(original_image, (round((original_image.height - original_image.width) / 2 ), 0))
result_image.save(fp=f"{filename}_edit.{extension}", quality=100, exif=original_image.info['exif'])
