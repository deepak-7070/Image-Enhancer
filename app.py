from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
import uuid
from enhancer import upscale_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enhance", methods=["POST"])
def enhance():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    # Save uploaded file
    filename = secure_filename(file.filename)
    unique_id = uuid.uuid4().hex
    input_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}_{filename}")
    output_path = os.path.join(OUTPUT_FOLDER, f"{unique_id}_enhanced.png")
    
    file.save(input_path)
    
    try:
        upscale_image(input_path, output_path)
        return send_file(output_path, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up uploaded file
        if os.path.exists(input_path):
            os.remove(input_path)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")
