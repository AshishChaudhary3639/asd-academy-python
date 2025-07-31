import os
# Base directory where folders will be created
base_path = "D:asif"

# # Create 100 folders
for i in range(1, 101):
    folder_name = f"ASD_folder_{i}"
    folder_path = os.path.join(base_path, folder_name)
    print(folder_path)
    os.makedirs(folder_path, exist_ok=True)
    
#     # Create a file inside the folder named file_i.txt
    file_path = os.path.join(folder_path, f"file_{i}.txt")

    with open(file_path, "w") as f:
        f.write(f"This is file number {i}\n")
        f.write("I am learning at ASD Academy")

# print("100 folders with files created successfully.")
