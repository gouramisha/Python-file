import os

print("📂 Current folder:", os.getcwd())     # Current working directory
print("📁 Files in this folder:", os.listdir())  # All files/folders

# Make new folder
os.mkdir("Skillans")
print("✅ Folder 'NewFolder' created!")
