import os
import shutil

# Step 1: Create folders
os.makedirs("original_folder", exist_ok=True)
os.makedirs("copied_folder", exist_ok=True)
os.makedirs("moved_folder", exist_ok=True)

# # Step 2: Create a file in the original folder
file_path = os.path.join("original_folder", "example.txt")
print(file_path)
with open(file_path, "w") as f:
    f.write("This is an example file for shutil operations.")

# Step 3: Copy the file to 'copied_folder'
shutil.copy(file_path, "copied_folder")

# Step 4: Move the file from 'original_folder' to 'moved_folder'
shutil.move(file_path, "moved_folder")

# print("File copied and moved successfully using shutil.")


#***********************************************************************

# Step 1: Create a folder and some files in it
folder_to_delete = "delete_me"
# os.makedirs(folder_to_delete, exist_ok=True)

# # Create some sample files
# for i in range(1, 4):
#     with open(os.path.join(folder_to_delete, f"file_{i}.txt"), "w") as f:
#         f.write(f"This is file {i}")

# print(f"Created folder '{folder_to_delete}' with files.")

# Step 2: Delete the entire folder
# shutil.rmtree(folder_to_delete)

# print(f"Folder '{folder_to_delete}' and all its contents have been deleted.")
