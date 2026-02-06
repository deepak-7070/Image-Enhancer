from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np

def upscale_image(input_path, output_path):
    try:
        # Load image using OpenCV first
        img_cv = cv2.imread(input_path)
        
        if img_cv is None:
            raise ValueError(f"Could not read image from {input_path}")
        
        h, w = img_cv.shape[:2]
        print(f"Original image size: {w}x{h}")
        
        # Step 1: Light denoise to reduce noise while preserving details
        img_cv = cv2.bilateralFilter(img_cv, 5, 50, 50)
        print("Light noise reduction applied")
        
        # Step 2: Upscale to 4K with best quality interpolation
        target_width = 3840
        scale_factor = target_width / w
        
        new_w = int(w * scale_factor)
        new_h = int(h * scale_factor)
        upscaled = cv2.resize(img_cv, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
        print(f"Upscaled image size: {upscaled.shape[1]}x{upscaled.shape[0]}")
        
        # Step 3: Apply Unsharp Mask for detail enhancement (preserves edges)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        upscaled_blurred = cv2.filter2D(upscaled, -1, kernel)
        upscaled = cv2.addWeighted(upscaled, 1.5, upscaled_blurred, -0.5, 0)
        print("Unsharp mask applied for detail enhancement")
        
        # Step 4: Apply adaptive local contrast enhancement
        lab = cv2.cvtColor(upscaled, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        # Apply CLAHE for local contrast and detail visibility
        clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
        l = clahe.apply(l)
        
        lab = cv2.merge((l, a, b))
        upscaled = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        print("Adaptive contrast enhancement applied")
        
        # Step 5: Convert to PIL for color enhancements
        upscaled_rgb = cv2.cvtColor(upscaled, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(upscaled_rgb)
        
        # Step 6: Strong sharpness for crisp details
        enhancer = ImageEnhance.Sharpness(pil_img)
        pil_img = enhancer.enhance(1.5)
        
        # Step 7: Enhance color vibrancy for attractiveness
        enhancer = ImageEnhance.Color(pil_img)
        pil_img = enhancer.enhance(1.2)
        
        # Step 8: Moderate brightness boost
        enhancer = ImageEnhance.Brightness(pil_img)
        pil_img = enhancer.enhance(1.1)
        
        # Step 9: Slight contrast for better definition
        enhancer = ImageEnhance.Contrast(pil_img)
        pil_img = enhancer.enhance(1.1)
        
        # Step 10: Save in high quality
        pil_img.save(output_path, quality=95)
        print(f"Enhanced image saved to {output_path}")
        
    except Exception as e:
        print(f"Error in upscale_image: {e}")
        raise


