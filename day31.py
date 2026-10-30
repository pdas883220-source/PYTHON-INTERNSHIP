# Day 31 - Python OS Module

import os

# Display the current working directory
print("Current Working Directory:", os.getcwd())

# Create a new folder
folder_name = "Python_Practice"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully.")
else:
    print("Folder already exists.")

# Display all files and folders
print("\nFiles and Folders:")
print(os.listdir())

# Check whether a folder exists
if os.path.exists(folder_name):
    print("\nPython_Practice folder exists.")