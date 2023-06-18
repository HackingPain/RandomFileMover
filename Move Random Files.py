# Created by: Domenic Laurenzi
# Purpose: The Randomly move a specoified number of folders to a different folder specified by the user. Frequently used randomly choose images for slideshows.

import os
import shutil
import random

def move_random_files(src_dir, dest_dir, num_files):
    # Get all files from source directory
    files = os.listdir(src_dir)

    # Filter out directories, only keep files
    files = [f for f in files if os.path.isfile(os.path.join(src_dir, f))]

    if num_files > len(files):
        print(f"Error: Not enough files in {src_dir} to move {num_files} files")
        return

    # Randomly select a number of files
    selected_files = random.sample(files, num_files)

    for file in selected_files:
        # construct full file path
        src_file_path = os.path.join(src_dir, file)
        dest_file_path = os.path.join(dest_dir, file)
        
        # Move each file to destination folder
        shutil.move(src_file_path, dest_file_path)

    print(f"Moved {num_files} files from {src_dir} to {dest_dir}")

# Usage
source_directory = r"input\source\directory\here"
destination_directory = r"input\destination\directory\here"

# Ask user for number of files to move
num_files_to_move = input("Enter the number of files you would like to move: ")

# Convert the user input to integer
num_files_to_move = int(num_files_to_move)

move_random_files(source_directory, destination_directory, num_files_to_move)
