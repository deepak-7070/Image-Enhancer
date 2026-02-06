from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import uuid
from enhancer import upscale_image

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "../uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "../outputs")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/enhance", methods=["POST"])
def enhance():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400

        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        # Secure and uniquify filenames to avoid collisions
        filename = secure_filename(file.filename)
        unique_input = f"{uuid.uuid4().hex}_{filename}"
        input_path = os.path.join(UPLOAD_FOLDER, unique_input)

        unique_output = f"enhanced_{uuid.uuid4().hex}.png"
        output_path = os.path.join(OUTPUT_FOLDER, unique_output)

        file.save(input_path)
        upscale_image(input_path, output_path)

        return send_file(output_path, mimetype="image/png")
    except Exception as e:
        print(f"Error in enhance: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')
