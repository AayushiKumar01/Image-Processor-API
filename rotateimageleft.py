import imp
from PIL import Image

class RotateLeft:
    def __init__(self, image):
        self.image = image

    def anticlockwise(cls, image):
        transformed_image = image.transpose(Image.TRANSPOSE)
        return transformed_image

        
