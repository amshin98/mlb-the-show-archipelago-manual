import shutil
import os

folder = "manual_mlbtheshow25_captaindonut"

# Name for the output (without extension)
zip_name = "manual_mlbtheshow25_captaindonut"

# Step 1: Create ZIP archive including the directory itself
shutil.make_archive(
    base_name=zip_name,
    format='zip',
    root_dir='.',          # parent directory
    base_dir=folder        # this folder will appear inside the zip
)

# Step 2: Rename .zip → .apworld
zip_file = f"{zip_name}.zip"
apworld_file = f"{zip_name}.apworld"

if os.path.exists(apworld_file):
    os.remove(apworld_file)

os.rename(zip_file, apworld_file)

print("Created:", apworld_file)
