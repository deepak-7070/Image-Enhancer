# Setup Instructions

## Install Missing Dependencies

You're missing some required packages. Install them with:

```bash
pip install opencv-python numpy flask-cors
```

Or install all at once:

```bash
pip install -r requirements.txt
```

## Verify Installation

```bash
pip list | findstr /i "flask opencv pillow numpy werkzeug"
```

You should see:
- Flask
- opencv-python
- Pillow
- numpy
- Werkzeug
- flask-cors

## Run the App

```bash
START.bat
```

Or manually:
```bash
cd html
python app.py
```

Then open: http://127.0.0.1:5000
