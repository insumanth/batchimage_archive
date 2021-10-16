"""Main module."""

# Imports
from pathlib import Path

def read_images(path, file_extension = []):

    file_names = []

    if file_extension == []:
        extensions = ['.jpg', '.png', '.bmp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.jpeg', '.jpe', '.jp2', '.tiff', '.tif']
    else:
        extensions = file_extension
    

    entries = Path(path)

    for entry in entries.iterdir():
        if entry.is_file() and entry.name.endswith(tuple(extensions)):
            file_names.append(entry.name)

    return file_names
