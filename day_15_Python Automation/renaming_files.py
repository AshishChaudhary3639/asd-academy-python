import os

# Set the folder path
# print("Testing the file")
# folder_path = "D:amir"
# # folder_path = r"D:\asif"
# prefix = "ASD Academy"
# # Loop through all files in the folder
# for filename in os.listdir(folder_path):
#     print(filename)
#     if filename.endswith(".txt"):
#         old_path = os.path.join(folder_path, filename)
#         new_filename = prefix + filename
#         print(new_filename)
#         new_path = os.path.join(folder_path, new_filename)
#         os.rename(old_path, new_path)
#         print(f"Renamed: {filename} -> {new_filename}")


folder_path = "D:amir"
new_base_name = "file_ASD_"
counter = 1

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        old_path = os.path.join(folder_path, filename)
        
        # Create new filename (e.g., file1.txt, file2.txt)
        new_filename = f"{new_base_name} {counter}.txt"
        new_path = os.path.join(folder_path, new_filename)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
        
        counter += 1




# # Set the main folder path
# main_folder_path = r"D:\asif"
# prefix = "ASD "

# Loop through all subfolders in the main folder
# for folder_name in os.listdir(main_folder_path):
#     subfolder_path = os.path.join(main_folder_path, folder_name)
#     print(subfolder_path)
#     # Check if it's a directory
#     if os.path.isdir(subfolder_path):
#         for filename in os.listdir(subfolder_path):
#             if filename.endswith(".txt"):
#                 old_path = os.path.join(subfolder_path, filename)
#                 new_filename = prefix + filename
#                 new_path = os.path.join(subfolder_path, new_filename)

#                 # Rename the file
#                 os.rename(old_path, new_path)
#                 print(f"Renamed: {old_path} -> {new_path}")
