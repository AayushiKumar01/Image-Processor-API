from PIL import Image

class ResizeImage:
    def __init__(self, image,height,width):
        self.image = image
        self.height = height
        self.width = width

    def resizeImage(cls, image, height, width):
        transformed_image = image.resize((width, height))
        return transformed_image

        
