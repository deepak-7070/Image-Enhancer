from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import os
from enhancer import upscale_image

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "../uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "../outputs")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(BASE_DIR, filename)

@app.route("/enhance", methods=["POST"])
def enhance():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400
        
        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400
        
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "enhanced.png")
        
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
