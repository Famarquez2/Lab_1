import os
import random


# To store the jpg photos in the list
class List:
    arr_cat = []
    arr_dog = []


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):
    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Traverse path and sort each file
    for i in file_list:
        pic = classify_pic(i)

        if pic < 0.5 and ".jpg" in i:  # Decides if classify_pic is a cat
            cat_list.append((path + "/" + i).replace("\\", "/"))  # If yes, append to cats list
        if pic > 0.5 and ".jpg" in i:  # Decides if classify_pic is a dog
            dog_list.append((path + "/" + i).replace("\\", "/"))  # If yes, append to dogs list

    # Where the pic is appended to
    List.arr_cat += cat_list
    List.arr_dog += dog_list

    # Traverse jpg pics
    for j in dir_list:
        process_dir(path + "/" + j) # Directs the pics to each list

    return cat_list, dog_list


def main():
    start_path = '/Users/Pic'  # current directory

    process_dir(start_path)
    p = List()
    print("Cats File: ", p.arr_cat)
    print("Dogs File: ", p.arr_dog)


main()
