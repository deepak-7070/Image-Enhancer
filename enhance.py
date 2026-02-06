#!/usr/bin/env python3
"""
Simple Image Enhancer - No server required
Usage: python enhance.py <image_path>
Or drag and drop an image onto this file
"""

import sys
import os
from enhancer import upscale_image

def main():
    print("=" * 50)
    print("AI Image Enhancer")
    print("=" * 50)
    
    # Get image path
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = input("Enter image path: ").strip('"')
    
    # Check if file exists
    if not os.path.exists(input_path):
        print(f"Error: File not found: {input_path}")
        input("Press Enter to exit...")
        return
    
    # Generate output path
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join("outputs", f"{base_name}_enhanced.png")
    
    # Ensure output folder exists
    os.makedirs("outputs", exist_ok=True)
    
    print(f"\nInput: {input_path}")
    print(f"Output: {output_path}")
    print("\nEnhancing image... (this may take a few seconds)")
    
    try:
        upscale_image(input_path, output_path)
        print(f"\n✓ Success! Enhanced image saved to: {output_path}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
