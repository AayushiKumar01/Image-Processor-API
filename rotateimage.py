from PIL import Image

class RotateImage:
    def __init__(self, image, rotationDegree):
        self.image = image
        self.rotationDegree = rotationDegree

    def rotate(cls, image, rotationDegree):
        if rotationDegree == 90:
            transformed_image = image.transpose(Image.ROTATE_90)
            return transformed_image

        elif rotationDegree == 180:
            transformed_image = image.transpose(Image.ROTATE_180)
            return transformed_image

        elif rotationDegree == 270:
             transformed_image = image.transpose(Image.ROTATE_270)
             return transformed_image
        
        else:
            return image
            
        

        
