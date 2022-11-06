from flask import Flask

UPLOAD_FOLDER = 'C:/Users/aayus/OneDrive/Pictures/Uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 3000 * 3000