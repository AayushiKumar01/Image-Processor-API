from PIL import Image

class Rotate180Degree:
    def __init__(self, image):
        self.image = image

    def rotate_180(cls, image):
        transformed_image = image.transpose(Image.ROTATE_180)
        return transformed_image

        
