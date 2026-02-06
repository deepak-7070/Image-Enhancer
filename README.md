# AI Image Enhancer

## 🚀 Quick Start for Beginners

### Step 1: Start the Flask Server
Open a terminal in the `html` folder and run:
```
python app.py
```

You should see:
```
Running on http://127.0.0.1:8000
```

### Step 2: Open in Browser
Copy and paste this URL in your browser:
```
http://127.0.0.1:8000
```

### Step 3: Use the App
1. Click "Choose File" to upload an image
2. Click "Enhance Image" button
3. Wait for processing
4. Click "Download Image" to save the enhanced version

## ⚠️ IMPORTANT FOR LIVE PREVIEW

If you're using VS Code Live Preview, it may open on a different port. Always use:
```
http://127.0.0.1:8000
```

## Project Structure

```
html/
├── app.py           # Flask application (runs on port 8000)
├── enhancer.py      # Image enhancement logic
├── index.html       # Web interface
├── style.css        # Styling
└── script.js        # JavaScript functionality
```

## Features

✅ Upload an image
✅ AI-powered image enhancement (4x upscaling)
✅ Automatic sharpness and contrast enhancement
✅ Download the enhanced image

## Troubleshooting

**Q: Live Preview shows errors?**
A: Ignore Live Preview. Always use: `http://127.0.0.1:8000`

**Q: Image not enhancing?**
A: 
1. Check Flask is running (see terminal)
2. Open browser console (F12) to see errors
3. Make sure image file is selected before clicking "Enhance Image"

**Q: Port already in use?**
A: Change the port in `app.py` line at the bottom:
```python
if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Change 8000 to another number
```
