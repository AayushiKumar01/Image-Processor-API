from PIL import Image

class Rotate270Degree:
    def __init__(self, image):
        self.image = image

    def rotate_270(cls, image):
        transformed_image = image.transpose(Image.ROTATE_270)
        return transformed_image

        
