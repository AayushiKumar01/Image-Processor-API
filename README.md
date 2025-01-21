The application that we're creating is a simple image processor. The end user provides an image in some format (your API will need to take this into account somehow) and allows the user to perform combinations of the following operations:

Flip horizontal and vertical
Rotate +/- n degrees
Convert to grayscale
Resize
Generate a thumbnail
Rotate left
Rotate right
The user can specify which operation or operations to perform on the image. Upon completion of the transform the user should have access to the resulting image file. Operations must be applied in an order specified by the caller.

