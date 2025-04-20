import io
from flask import Flask, send_file, render_template, url_for
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

app = Flask(__name__)
# Define the scope and load your service account credentials:
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'credentials/service-account.json'  # Replace with your credentials file path

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
drive_service = build('drive', 'v3', credentials=credentials)

# An endpoint to download and serve an image file stored in Google Drive.
@app.route('/image/1lDyO_KjIMjXYCakrCXXZdyzrKV9HIO9Z')
def get_image(file_id):
    request = drive_service.files().get_media(fileId=file_id)
    file_stream = io.BytesIO()
    downloader = MediaIoBaseDownload(file_stream, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    file_stream.seek(0)
    return send_file(file_stream, mimetype='image/jpg')

# Route to render the machines page.
@app.route('/technologies')
def machines():
    # Replace these file IDs with the actual file IDs from your Google Drive.
    file_ids = {
        'product1': '1lDyO_KjIMjXYCakrCXXZdyzrKV9HIO9Z',
        'product2': '1s1D6eDMhQU43_MmjHFjG1A9hESBwGT2Y',
        'product3': '1bnHStAXzITPeSj-4LzSscWL1wRQONgaH'
    }
    return render_template('machines.html', file_ids=file_ids)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product-center')
def product_center():
    return render_template('product.html')

#@app.route('/technologies')
#def technologies():
#    return render_template('machines.html')


@app.route('/contact-us')
def contact():
    return render_template('contact.html')

@app.route('/distributor')
def distributor():
    return "<h1>Distributor Page</h1>"  # Or render a template if you have one

@app.route('/support')
def support():
    return "<h1>Support Page</h1>"

@app.route('/news')
def news():
    return "<h1>News Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
