
from image_sorter import sort_images

def main(base_folder, new_base_folder):
    return sort_images(base_folder, new_base_folder)

if __name__ == "__main__":
    main(base_folder="folders", new_base_folder="result")
