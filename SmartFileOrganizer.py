# Practicing Automation, File I/O, and OS Library

import os
import shutil

def organize_folder(target_directory):
    # 1. Define folder mapping
    extensions = {
        ".py": "Python_Scripts",
        ".txt": "Documents",
        ".png": "Images",
        ".jpg": "Images",
        ".pdf": "Documents"
    }

    print(f"---  Organizing: {target_directory} ---")

    # 2. Iterate through files in the directory
    for filename in os.listdir(target_directory):
        filepath = os.path.join(target_directory, filename)
        
        # Skip directories, only process files
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1].lower()
            
            if file_ext in extensions:
                subdir = extensions[file_ext]
                subdir_path = os.path.join(target_directory, subdir)
                
                # 3. Create folder if it doesn't exist
                if not os.path.exists(subdir_path):
                    os.makedirs(subdir_path)
                
                # 4. Move the file
                shutil.move(filepath, os.path.join(subdir_path, filename))
                print(f"Moved: {filename} -> {subdir}")

if __name__ == "__main__":
    # You can change '.' to any specific folder path you want to clean up
    organize_folder('.')