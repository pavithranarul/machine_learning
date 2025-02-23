import sys
import os
sys.path.append("../src")  # Add src/ directory to path
from flask import Flask, render_template, request
from predict import predict_soil

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the upload directory exists

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)  # Save file to the uploads folder

            soil, crops, fertilizers = predict_soil(file_path)
            return render_template("index.html", soil=soil, crops=crops, fertilizers=fertilizers, image_path=file_path)

    return render_template("index.html", soil=None)

if __name__ == "__main__":
    app.run(debug=True)
