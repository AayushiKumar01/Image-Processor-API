from PIL import Image

class FlipHorizontal:
    def __init__(self, image):
        self.image = image

    def flipHorizontal(cls, image):
        transformed_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        return transformed_image

        
