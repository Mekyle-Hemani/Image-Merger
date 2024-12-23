import tkinter as tk
from tkinter import filedialog
import os

def selectFiles(title="Select Files", forceFileTypes=True, startDir=None):
    root = tk.Tk()
    root.withdraw()

    fileTypes = []

    if forceFileTypes == False:
        fileTypes.append(("All Files", "*.*"))
    else:
        fileTypes.append(("Images", "*.jpg;*.jpeg;*.png;*.webp;"))

    selectedFiles = filedialog.askopenfilenames(
        title=title,
        filetypes=fileTypes,
        initialdir=startDir
    )
    
    if selectedFiles:
        result = []
        for file in selectedFiles:
            result.append(file)
        return result, os.path.dirname(result[len(result)-1])
    else:
        return None, None

def selectFolder(title="Select Folder", startDir=None):
    root = tk.Tk()
    root.withdraw()

    selectedFolder = filedialog.askdirectory(
        title=title,
        initialdir=startDir
    )

    if selectedFolder:
        return selectedFolder
    else:
        return None
