from django.core.exceptions import ValidationError
from PIL import Image


def validate_image_size(value):
    # Max size in bytes (500 KB)
    max_size = 500 * 1024

    if value.size > max_size:
        raise ValidationError('Image file size must be less than 500 KB.')


def validate_image_type(value):
    try:
        image = Image.open(value)
        if image.format.lower() not in ['jpeg', 'png', 'gif']:
            raise ValidationError('Invalid image format. Supported formats: JPEG, PNG, GIF.')
    except Exception as e:
        raise ValidationError('Invalid image file.')
