from PIL import Image

class RotateRight:
    def __init__(self, image):
        self.image = image

    def clockwise(cls, image):
        transformed_image = image.transpose(Image.TRANSVERSE)
        return transformed_image

        
