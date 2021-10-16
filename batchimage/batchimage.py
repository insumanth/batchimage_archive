"""Main module."""

# Imports
import numpy as np
import cv2 
import multiprocessing

from pathlib import Path

# Flags

GREY_SCALE = 0



def process(input_directory, output_directory, parallel_tasks, operation_flag, *args):
    
    file_list = read_images(input_directory)

    files_count = len(file_list)
    files_per_task = int(files_count/parallel_tasks)

    if operation_flag == 0:
        pass




# Developer Functions



def read_images(path, file_extension = []):

    file_names = []

    if not file_extension :
        extensions = ('.jpg', '.png', '.bmp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.jpeg', '.jpe', '.jp2', '.tiff', '.tif')
    else:
        extensions = tuple(file_extension)
    

    entries = Path(path)

    for entry in entries.iterdir():
        if entry.is_file() and entry.name.endswith(extensions):
            file_names.append(entry.name)

    return file_names



def grayscale():
    pass
