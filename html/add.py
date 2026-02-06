from PIL import Image, ImageEnhance
import cv2
import numpy as np

def upscale_image(input_path, output_path):
    # Load image using PIL
    image = Image.open(input_path).convert("RGB")
    
    # Upscale using OpenCV
    img_cv = cv2.imread(input_path)
    h, w = img_cv.shape[:2]
    
    # Upscale 4x
    upscaled = cv2.resize(img_cv, (w*4, h*4), interpolation=cv2.INTER_CUBIC)
    
    # Enhance sharpness and contrast
    pil_img = Image.fromarray(cv2.cvtColor(upscaled, cv2.COLOR_BGR2RGB))
    enhancer = ImageEnhance.Sharpness(pil_img)
    pil_img = enhancer.enhance(1.5)
    
    enhancer = ImageEnhance.Contrast(pil_img)
    pil_img = enhancer.enhance(1.2)
    
    pil_img.save(output_path)
