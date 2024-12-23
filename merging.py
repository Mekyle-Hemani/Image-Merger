from PIL import Image
import os

def merge(file_paths, output_pdf):
    images = []

    for file_path in file_paths:
        try:
            img = Image.open(file_path).convert("RGB")
            images.append(img)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    try:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
    except Exception as e:
        print(f"Error creating PDF: {e}")