# AI Image Enhancer - Web Tool

Beautiful web interface to upscale and enhance images to 4K resolution using AI.

## Features

- 🎨 Modern, clean web interface
- 📤 Drag & drop or click to upload
- 🚀 4K upscaling (3840px width)
- 🤖 AI-powered enhancement
- 💾 One-click save
- ⚡ Fast processing

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Web App

**Double-click:**
```
run.bat
```

**Or manually:**
```bash
python app.py
```

### 3. Use the Tool

1. Browser opens automatically at http://127.0.0.1:5000
2. Click or drag & drop an image
3. Click "Enhance Image"
4. Wait a few seconds
5. Click "Save Enhanced Image"

## How It Works

The tool applies advanced AI enhancement:

1. **Noise Reduction** - Bilateral filtering
2. **4K Upscaling** - Lanczos interpolation
3. **Detail Enhancement** - Unsharp masking
4. **Contrast Boost** - CLAHE algorithm
5. **Color & Sharpness** - Final polish

## Project Structure

```
Image-Enhancer/
├── app.py               # Flask web server
├── enhancer.py          # AI enhancement engine
├── templates/
│   └── index.html       # Web interface
├── uploads/             # Temporary uploads
├── outputs/             # Enhanced images
├── run.bat              # Quick launcher
├── enhance.py           # CLI version (optional)
├── enhance.bat          # CLI launcher (optional)
└── requirements.txt     # Dependencies
```

## Two Ways to Use

### Web Interface (Recommended)
```bash
python app.py
```
Beautiful UI with drag & drop

### Command Line (Alternative)
```bash
python enhance.py image.jpg
```
Simple CLI for batch processing

## Requirements

- Python 3.7+
- 2GB+ RAM
- Modern web browser

## Supported Formats

- Input: JPG, PNG, BMP, TIFF, WebP
- Output: PNG (high quality)

## Tips

- Larger images take longer to process
- Enhanced images are high quality PNG files
- Original images are never modified
- Close browser tab when done (server keeps running)

## License

MIT License - Free to use and modify
