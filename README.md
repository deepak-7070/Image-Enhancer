# AI Image Enhancer

AI-powered web application that upscales and enhances images to 4K resolution with advanced image processing techniques.

## Features

- 🚀 4K upscaling (3840px width)
- 🎨 AI-powered enhancement (noise reduction, sharpness, contrast)
- 🖼️ Before/After comparison slider
- 📥 Download enhanced images
- 🌐 Clean web interface

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

**Windows:**
```bash
START.bat
```

**Manual:**
```bash
python app.py
```

### 3. Open in Browser

Navigate to: `http://127.0.0.1:5000`

## Usage

1. Click "Choose File" and select an image
2. Click "Enhance" button
3. Wait for processing (may take a few seconds)
4. Click "Download" to save the enhanced image
5. Use "Show Comparison" to see before/after

## Project Structure

```
Image-Enhancer/
├── app.py                  # Flask server
├── enhancer.py             # Image processing logic
├── templates/
│   └── index.html          # Web interface
├── static/
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
├── uploads/                # Temporary uploaded images
├── outputs/                # Enhanced images
├── requirements.txt        # Python dependencies
├── START.bat               # Windows launcher
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Technology Stack

- **Backend**: Flask, Python 3.x
- **Image Processing**: OpenCV, Pillow
- **Frontend**: HTML5, CSS3, JavaScript

## Enhancement Pipeline

1. Bilateral filtering (noise reduction)
2. Lanczos interpolation (4K upscaling)
3. Unsharp masking (detail enhancement)
4. CLAHE (adaptive contrast)
5. Color, brightness, and sharpness adjustments

## Requirements

- Python 3.7+
- 2GB+ RAM recommended
- Modern web browser

## License

MIT License - Feel free to use and modify.
