from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np

def upscale_image(input_path, output_path):
    try:
        # Load image
        img = cv2.imread(input_path)
        if img is None:
            raise ValueError(f"Could not read image from {input_path}")
        
        h, w = img.shape[:2]
        print(f"Original: {w}x{h}")
        
        # Calculate smart scale (max 2x for quality, or fit to reasonable size)
        max_dimension = max(w, h)
        if max_dimension < 1920:
            scale = 2.0  # 2x upscale for small images
        else:
            scale = min(2.0, 3840 / max_dimension)  # Cap at 2x or 4K width
        
        new_w = int(w * scale)
        new_h = int(h * scale)
        
        # High-quality upscaling with INTER_CUBIC (better than LANCZOS for photos)
        upscaled = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
        print(f"Upscaled: {new_w}x{new_h}")
        
        # Gentle noise reduction (preserve details)
        denoised = cv2.fastNlMeansDenoisingColored(upscaled, None, 3, 3, 7, 21)
        
        # Subtle sharpening with unsharp mask
        gaussian = cv2.GaussianBlur(denoised, (0, 0), 2.0)
        sharpened = cv2.addWeighted(denoised, 1.5, gaussian, -0.5, 0)
        
        # Gentle contrast enhancement (avoid over-processing)
        lab = cv2.cvtColor(sharpened, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
        l = clahe.apply(l)
        
        enhanced = cv2.merge((l, a, b))
        enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
        
        # Convert to PIL for final touches
        rgb = cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb)
        
        # Subtle enhancements (avoid over-saturation)
        pil_img = ImageEnhance.Sharpness(pil_img).enhance(1.1)
        pil_img = ImageEnhance.Color(pil_img).enhance(1.05)
        pil_img = ImageEnhance.Contrast(pil_img).enhance(1.05)
        
        # Save with maximum quality
        pil_img.save(output_path, 'PNG', quality=100, optimize=False)
        print(f"Saved: {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")
        raise


