from PIL import ImageOps

class GrayscaleImage:
    def __init__(self, image):
        self.image = image

    def grayscale(cls, image):
        transformed_image = ImageOps.grayscale(image)
        return transformed_image

        
