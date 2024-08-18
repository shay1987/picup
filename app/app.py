from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Choose a project and bucket
project_id = '<your_project_id>'
bucket_name = '<your_bucket_name>'

# Create a storage client
storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket(bucket_name)

@app.route('/')
def index():
    """
    List files in the Google Cloud Storage bucket.
    ---
    responses:
      200:
        description: A list of files in the bucket.
        content:
          text/html:
            schema:
              type: string
    """
    blobs = bucket.list_blobs()
    return render_template('index.html', blobs=blobs)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    Upload a file to the Google Cloud Storage bucket.
    ---
    consumes:
      - multipart/form-data
    parameters:
      - in: formData
        name: file
        type: file
        required: true
        description: The file to upload.
    responses:
      302:
        description: Redirect to the index page after upload.
    """
    if request.method == 'POST':
        file = request.files['file']
        blob = bucket.blob(file.filename)
        blob.upload_from_string(file.read(), content_type=file.content_type)
        return redirect(url_for('index'))

    return render_template('upload.html')

@app.route('/delete/<filename>')
def delete(filename):
    """
    Delete a file from the Google Cloud Storage bucket.
    ---
    parameters:
      - in: path
        name: filename
        type: string
        required: true
        description: The name of the file to delete.
    responses:
      302:
        description: Redirect to the index page after deletion.
    """
    blob = bucket.blob(filename)
    blob.delete()
    return redirect(url_for('index'))

@app.route('/serve_image/<filename>')
def serve_image(filename):
    """
    Serve an image from the Google Cloud Storage bucket.
    ---
    parameters:
      - in: path
        name: filename
        type: string
        required: true
        description: The name of the image file to serve.
    responses:
      302:
        description: Redirect to the image URL in Google Cloud Storage.
    """
    return redirect(f"https://storage.googleapis.com/{bucket_name}/{filename}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
