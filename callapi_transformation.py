import os
import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from PIL import Image
import io

headers = {'Content-type': 'multipart/form-data'}
payload = {"transformations":"thumbnail"}
url = 'http://127.0.0.1:5000/transformations'
image_file = 'C:\\Users\\aayus\\OneDrive\\Pictures\\thumb.png'

multipart_data = MultipartEncoder(
    fields={
            # a file upload field
            'file': ('thumb.png', open(image_file, 'rb'), 'text/plain'),
            # plain text fields
            'transformations': 'grayscale,resize,rotateDegrees_90',
            
           }
    )

response = requests.post(url, data=multipart_data,
                  headers={'Content-Type': multipart_data.content_type})

image = Image.open(io.BytesIO(response.content))
image.show()
image.save('C:\\Users\\aayus\\OneDrive\\Pictures\\CPSC 5200 DEMO - IMAGES\\Saved Images\\sample.png')