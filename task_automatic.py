import os
import shutil

source_folder = "MyPhotos"
destination_folder = "JPG_Files"

os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

print("All JPG files moved successfully!")