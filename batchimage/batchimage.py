"""Main module."""

# Imports
import numpy as np
import cv2 
import multiprocessing
import time

from pathlib import Path
from math import ceil
from tqdm import tqdm



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


def get_operation(option):

    if option == 0:
        return convert_to_greyscale
    elif option == 1:
        return 
    elif option == 2:
        return 
    elif option == 3:
        return 
    elif option == 4:
        return 
    elif option == 5:
        return 
    elif option == 6:
        return 
    elif option == 7:
        return 
    elif option == 8:
        return 
    elif option == 9:
        return 
    else:
        return None
    

def convert_to_greyscale(files, input_directory, output_directory):
    
    for image_file in files:

        read_file_name = "{}{}".format(input_directory, image_file)
        write_file_name = "{}{}{}".format(output_directory, 'greyscale_' , image_file)

        image = cv2.imread(read_file_name, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(write_file_name, image)

def convert_to_x():
    pass



# ==========================================================================================
#                                      Entry Function
# ==========================================================================================

def process(input_directory, output_directory, parallel_tasks, option, **kwargs):

    start_time = time.time()

    # ++ TODO : REMOVE ++#
    operation = get_operation(option)

    file_list = read_images(input_directory)
    all_task = create_processes(file_list, input_directory, output_directory, parallel_tasks, operation)

    for task in all_task:
        task.start()

    for task in all_task:
        task.join()

    end_time = time.time()
    time_taken = end_time - start_time
    return "The Task Completed in " + str(time_taken) + " Seconds"

