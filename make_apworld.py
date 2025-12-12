import shutil
import os

# Name of the file or folder you want to zip
source = "manual_mlbtheshow25_captaindonut"

# Name of the output without extension
zip_name = "manual_mlbtheshow25_captaindonut"

# Step 1: Create ZIP file
shutil.make_archive(zip_name, 'zip', source)

# Step 2: Rename ZIP to .apworld
zip_file = f"{zip_name}.zip"
apworld_file = f"{zip_name}.apworld"

# Remove existing .apworld if it exists
if os.path.exists(apworld_file):
    os.remove(apworld_file)

os.rename(zip_file, apworld_file)

print("Created:", apworld_file)
