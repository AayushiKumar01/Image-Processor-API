from PIL import Image

class ImageThumbnail:
    def __init__(self, image):
        self.image = image

    def thumbnail(cls, image):
        MAX_SIZE = (100, 100)
        image.thumbnail(MAX_SIZE)
        return image

        
