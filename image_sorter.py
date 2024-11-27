import os

def get_path(parts):
    return "/".join(parts)


def sort_images(base_folder, new_base_folder):
    folders = os.listdir(base_folder)
    os.mkdir(new_base_folder)
    for folder in folders:
        sub_folders = os.listdir(get_path([base_folder, folder]))
        os.mkdir(get_path([new_base_folder, folder]))
        for sub_folder in sub_folders:
            files = os.listdir(get_path([base_folder, folder, sub_folder]))
            for index in range(0, len(files)):
                new_path = get_path([new_base_folder, folder, str(index + 1)])
                if not os.path.exists(new_path):
                    os.mkdir(new_path)
                old = get_path([base_folder, folder, sub_folder, files[index]])
                new = get_path([new_path, sub_folder + "." + files[index].split(".")[1]])
                os.replace(old, new)
