from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_bootstrap import Bootstrap

import os
import base64
from io import BytesIO


app = Flask(__name__)
Bootstrap(app)

# Flask app creates a folder called "instance" when it is run.

# Create path to "uploads" directory (or folder) inside Flask's instance folder
uploads_dir = os.path.join(app.instance_path, 'uploads')
# If the path "instance\uploads" doesn't exist, create it.
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/save_image', methods=['GET', 'POST'])
def save_image():
    app.logger.info("works")
    if request.method == "POST":
        if request.files:
            app.logger.info("files...")
            image = request.files["image"]
            app.logger.info(image.filename)
            if image.filename != "":
                # To save the image in a folder:
                image.save(os.path.join(uploads_dir, image.filename))

                # Convert image to base64
                img_str = base64.b64encode(image.getvalue())

                # Send image as base64
                return render_template("show_image.html", sent_image=img_str.decode('utf-8'))
    return render_template('base.html')


if __name__ == "__main__":
  app.run()
