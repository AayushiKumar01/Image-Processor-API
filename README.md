# Image Processor API

A RESTful API built with Python and Flask that allows users to upload images and apply multiple image transformations in a single request. The API validates uploaded files and transformation parameters, processes operations in the requested order, and returns the resulting image.

## Features

- Upload images in PNG, JPG, and JPEG formats.
- Apply multiple transformations in a single request.
- Retrieve the list of supported transformations through an API endpoint.
- Validate uploaded files and transformation parameters.
- Return clear error messages for invalid requests.
- Use the Factory Design Pattern to organize image transformation operations.

## Tech Stack

- **Language:** Python 3.10.2
- **Framework:** Flask
- **Image Processing Library:** Pillow
- **Architecture:** Client-server architecture using REST APIs
- **Design Pattern:** Factory Design Pattern

## Architecture

The application follows a client-server architecture. Clients send HTTP requests to the Flask server, which validates the request, processes the requested image transformations, and returns the response.

The API follows REST principles and uses stateless communication, meaning each request is handled independently.

The image processing workflow is:

1. Receive the uploaded image and transformation parameters.
2. Validate that an image file is present.
3. Verify that the uploaded file has an allowed extension.
4. Validate the requested transformations and their parameters.
5. Apply the transformations in the order specified by the client.
6. Return the transformed image to the client.

## API Endpoints

### 1. Get Supported Transformations

`GET /transformationslist`

Returns the list of supported image transformations and the parameter formats required for operations such as resizing and rotation.

**Request parameters:** None

**Example request:**

```http
GET http://127.0.0.1:5000/transformationslist
```

### 2. Transform an Image

`POST /transformations`

Accepts an image file and a list of transformations, applies the requested operations in order, and returns the processed image.

**Request parameters:**

| Parameter | Description |
|---|---|
| `file` | Image file to process. Supported formats: PNG, JPG, JPEG. |
| `transformations` | List of transformation operations to apply. |

Use a multipart form-data request to upload the image and provide the transformation parameters.

## Supported Transformations

| Transformation | Description |
|---|---|
| `anticlockwise` | Rotates the image anticlockwise. |
| `clockwise` | Rotates the image clockwise. |
| `fliphorizontal` | Flips the image horizontally. |
| `flipvertical` | Flips the image vertically. |
| `resizeWidthHeight_100_50` | Resizes the image to a width of 100 and height of 50. Replace these values with the desired dimensions. |
| `rotateDegrees_90` | Rotates the image by the specified number of degrees. Replace the example value as needed. |
| `grayscale` | Converts the image to grayscale. |
| `thumbnail` | Generates a thumbnail of the image. |

Multiple transformations can be supplied in a single request. They are applied in the order specified.

For parameterized transformations, dimensions and rotation degrees are encoded in the transformation value using underscores (`_`).

Examples:

- `resizeWidthHeight_100_50`
- `rotateDegrees_90`

## Error Handling

The API validates incoming requests and returns HTTP `400 Bad Request` responses for invalid input.

| Scenario | Error message |
|---|---|
| No file part in the request | `No file part in the request` |
| File provided but not selected | `No file selected for uploading` |
| Unsupported file type | `Allowed file types are png, jpg, jpeg` |
| Missing transformations | `please enter required transformations.` |
| Invalid transformation | `please enter valid transformation(s).` |
| Invalid resize dimensions | `Please provide valid integers for height and width.` |
| Invalid rotation degrees | `Please provide valid integers for degree.` |

## Design Pattern

The project uses the **Factory Design Pattern** to organize image transformations.

Instead of maintaining separate API endpoints for individual transformations, the implementation consolidates transformation requests into a single endpoint and uses individual transformation classes to handle different operations.

This approach provides a structured way to select and apply transformations while keeping the API interface consistent.

## Implementation Notes and Trade-offs

- **Pillow:** Pillow was selected for image processing after initially exploring OpenCV.
- **Unified transformation endpoint:** Individual transformation APIs were consolidated into one endpoint to support multiple operations through a consistent interface.
- **Transformation parameters:** Resize dimensions and rotation degrees are encoded alongside the operation name, separated by underscores.
- **JPEG handling:** JPG images are converted to PNG internally to address a format-related `KeyError` encountered during processing.



