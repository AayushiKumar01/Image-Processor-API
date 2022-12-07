he application that we're creating is a simple image processor. The end user provides an image in some format (your API will need to take this into account somehow) and allows the user to perform combinations of the following operations:

Flip horizontal and vertical
Rotate +/- n degrees
Convert to grayscale
Resize
Generate a thumbnail
Rotate left
Rotate right
The user can specify which operation or operations to perform on the image. Upon completion of the transform the user should have access to the resulting image file. Operations must be applied in an order specified by the caller.

The application should be designed to be cloud-hosted. Transformation pipelines should run quickly and the caller should not have to wait an unreasonable time. You should consider storage and security issues if you keep a copy of the source or resulting image "on the service".

For the implementation component you are not required to actually run the application / service in the cloud. However, you should chose a language / framework that allows you to run as if you're running in the cloud. That is, your application (the service and the client) needs to run on your local device.

You have two user classes:

application developers who will interact with your public API so that they can use your image processor application
anonymous consumers via a web browser / application (that you provide)
We are focusing on the first class primarily, but the second class should not be discounted or ignored.
