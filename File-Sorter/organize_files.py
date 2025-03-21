import os
import shutil

# Define the path of the directory you want to organize
directory_path = '/Users/zainkhan/Documents'  # This is the directory path you specified

# Keywords to search for and their corresponding target folders
keywords_to_folders = {
    'ERP': 'ERP',
    'R-CUBED': 'R-CUBED'
}

# Function to organize files
def organize_files_by_content(directory_path):
    # Ensure target folders exist
    for folder in keywords_to_folders.values():
        target_folder = os.path.join(directory_path, folder)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Ensure it's a file and not a directory
        if os.path.isfile(file_path):
            try:
                # Open and read the file
                with open(file_path, 'r', errors='ignore') as file:
                    content = file.read()
                    
                    # Check for keywords in the file content
                    for keyword, folder in keywords_to_folders.items():
                        if keyword in content:
                            # Move the file to the corresponding folder
                            target_folder = os.path.join(directory_path, folder)
                            target_path = os.path.join(target_folder, filename)
                            
                            shutil.move(file_path, target_path)
                            print(f"Moved '{filename}' to '{folder}' folder.")
                            break  # Stop checking after the first match to avoid multiple moves
            except Exception as e:
                print(f"Could not read file {filename}: {e}")

# Run the function
organize_files_by_content(directory_path)
