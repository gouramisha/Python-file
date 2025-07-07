import shutil

# Copy a file
shutil.copy("data.txt", "data_backup.txt")

# Move a file
shutil.move("data_backup.txt", "backup_folder/data_backup.txt")

# Delete a folder
shutil.rmtree("old_backup")

# Make a zip file
shutil.make_archive("project_backup", "zip", "project")
