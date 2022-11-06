
from xmlrpc.client import ResponseError
from rotateimageleft import RotateLeft
from rotateimageright import RotateRight
from flipimagehorizontal import FlipHorizontal
from flipimagevertical import FlipVertical
from imagethumbnail import ImageThumbnail
from grayscaleimage import GrayscaleImage
from resizeimage import ResizeImage
from rotateimage import RotateImage

class ImageTransformationsDecider:
    def __init__(self, image, transformation):
        self.image = image
        self.transformation = transformation
        

    def applyTransformation(cls, image, trasformation):
        if trasformation == "anticlockwise":
            classObject = RotateLeft(image)
            return classObject.anticlockwise(image)

        elif trasformation == "clockwise":
            classObject = RotateRight(image)
            return classObject.clockwise(image)

        elif trasformation == "flipvertical":
            classObject = FlipVertical(image)
            return classObject.flipVertical(image)

        elif trasformation == "fliphorizontal":
            classObject = FlipHorizontal(image)
            return classObject.flipHorizontal(image)
        
        elif trasformation == "thumbnail":
            classObject = ImageThumbnail(image)
            return classObject.thumbnail(image)
        
        
        elif trasformation == "grayscale":
            classObject = GrayscaleImage(image)
            return classObject.grayscale(image)

        elif "resizeWidthHeight" in trasformation:
            size = trasformation.split("_")
            try:
                int(size[1])
                int(size[2])
            except ValueError:
                raise ValueError("Please provide valid integers for height and width.")
            
            size = trasformation.split("_")    
            classObject = ResizeImage(image,int(size[1]),int(size[2]))
            return classObject.resizeImage(image,int(size[1]),int(size[2]))


        elif "rotateDegrees" in trasformation:

            degree = trasformation.split("_")
            try:
                int(degree[1])
               
            except ValueError:
                raise ValueError("Please provide valid integers for degrees.")

            degree = trasformation.split("_")    
            classObject = RotateImage(image,int(degree[1]))
            return classObject.rotate(image,int(degree[1]))

        else:
            return image
    