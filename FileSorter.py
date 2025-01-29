import os
import shutil

folder_path = "/users/rowanjames/Downloads"
file_names = os.listdir(folder_path)

#stores file types
file_types = []
file_with_types = []
for name in file_names:
    
    if "DS_Store" in name or "localized" in name:
        continue

    file_path = os.path.join(folder_path, name)

    if os.path.isfile(file_path):
        ext = name.split('.')[-1]
        if ext not in file_types:
            file_types.append(ext)
        file_with_types.append((name, ext))
    elif os.path.isdir(file_path):
        if "Folders" not in file_types:
            file_types.append("Folders")
        file_with_types.append((name, "Folders"))

#create folders
for ft in file_types:
    new_folder_path = os.path.join(folder_path, ft + " Files")
    os.makedirs(new_folder_path, exist_ok=True)

# move files into folders
for f in file_with_types:
    source_file = os.path.join(folder_path, f[0])
    destination_path = os.path.join(folder_path, f[1] + " Files", f[0])
    shutil.move(source_file, destination_path)

