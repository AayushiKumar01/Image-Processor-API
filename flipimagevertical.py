from PIL import Image

class FlipVertical:
    def __init__(self, image):
        self.image = image

    def flipVertical(cls, image):
        transformed_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        return transformed_image

        
