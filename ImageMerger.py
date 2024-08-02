import tkinter as tk
from tkinter import filedialog
import os
from PyPDF2 import PdfWriter, PdfReader
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime
import time

extensions = [".pdf", ".PDF", ".jpg", ".JPG", ".webp", ".WEBP", ".png", ".PNG"]

ORANGE = '38;5;208'
BLUE = '34'
YELLOW = '33'
GREEN = '32'
RED = '31'

combine = []
next = []

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def select_folder(windowtitle):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(initialdir='/', title=windowtitle)
    if folder_path:
        return folder_path
    else:
        return select_folder(windowtitle)

def find_files(directory):
    file_count = 0
    if os.path.isdir(directory):
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isfile(full_path):
                file_count += 1
                _, ext = os.path.splitext(entry)
                ext = ext.lower()
                if ext in [e.lower() for e in extensions]:
                    print_colored(f"{entry}, {ext}", GREEN)
                    combine.append(full_path)
                else:
                    print_colored(f"{entry}, {ext}", RED)
            elif os.path.isdir(full_path):
                print_colored(f"{entry}, {full_path}", BLUE)
                next.append(full_path)
    
    if len(combine) == 0:
        combine.append(None)
    if len(next) == 0:
        next.append(None)

    return [combine, next]

def add_image_to_pdf(image_path, pdf_writer):
    try:
        image = Image.open(image_path)
        width, height = image.size
        c = canvas.Canvas("temp_image.pdf", pagesize=(width, height))
        c.drawImage(image_path, 0, 0, width, height)
        c.save()
        pdf_reader = PdfReader("temp_image.pdf")
        pdf_writer.add_page(pdf_reader.pages[0])
        os.remove("temp_image.pdf")
        print_colored(f"Added image: {image_path}", ORANGE)
    except Exception as e:
        print(f"Error adding image to PDF: {e}")

def combine_files(output_filename, input_files):
    pdf_writer = PdfWriter()

    for file in input_files:
        if file and file.lower().endswith('.pdf'):
            try:
                pdf_reader = PdfReader(file)
                for page_num in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page_num])
            except Exception as e:
                print(f"Error reading PDF file {file}: {e}")
        elif file and file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            add_image_to_pdf(file, pdf_writer)
        else:
            print(f"Unsupported file format or invalid path: {file}")

    with open(output_filename, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

result = find_files(select_folder("Select Files"))

output_filename = f"{select_folder('Select Output Location')}/CombinedPDF_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

countdown = 5

while countdown!=0:
    print_colored(f"Combining given files in {countdown} seconds", YELLOW)
    time.sleep(1)
    countdown -= 1

combine_files(output_filename, result[0])

print_colored(f"Done combining files at: {output_filename}", BLUE)