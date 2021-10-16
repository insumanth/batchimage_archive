"""Main module."""

# Imports
import numpy as np
import cv2 
import multiprocessing
import time

from pathlib import Path
from math import ceil



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


def create_processes(file_list, input_directory, output_directory, parallel_tasks, operation):
    process_list = []

    files_count = len(file_list)
    files_per_process_count = ceil(files_count/parallel_tasks)

    file_list_process = [file_list[i:i + files_per_process_count] for i in range(0, files_count, files_per_process_count)]

    for each_list in file_list_process:
        task = multiprocessing.Process(target=operation, args=(each_list, input_directory, output_directory))
        process_list.append(task)
    
    return process_list


    

def convert_to_greyscale(files, input_directory, output_directory):
    pass

def convert_to_x():
    pass

# ==========================================================================================
#                                      Flags
# ==========================================================================================

GREY_SCALE = convert_to_greyscale


# ==========================================================================================
#                                      Entry Function
# ==========================================================================================

def process(input_directory, output_directory, parallel_tasks, operation, *args):

    start_time = time.time()

    file_list = read_images(input_directory)
    all_task = create_processes(file_list, input_directory, output_directory, parallel_tasks, operation)

    for task in all_task:
        task.start()

    for task in all_task:
        task.join()

    end_time = time.time()
    time_taken = start_time - end_time
    print("The Task Completed in " + str(time_taken) + " Seconds")

