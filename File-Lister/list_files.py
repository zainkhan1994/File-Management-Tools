import os

# List all files in the current directory
files = os.listdir('.')
print("Files in the current directory:")
for file in files:
    print(file)
