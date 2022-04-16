import os
import re

# Current directory complet path
current_path = os.path.dirname(os.path.realpath(__file__))
files = os.listdir()

def get_extension(files):
    ext = list()
    for i in files:
        ext_ = i.split('.')[-1]
        if os.path.isfile(current_path + "/" + i):
            if not ext_ in ext:
                ext.append(ext_)
    return ext

def create_folder(path, ext):
    for i in ext:
        if not os.path.exists(path + "/" + i):
            os.makedirs(i)

def move_files(files):
    for i in files:
        ext_ = i.split('.')[-1]
        if os.path.isfile(current_path + "/" + i):
            os.rename(current_path + "/" + i, current_path + "/" + ext_ + "/" + i)

if __name__ == "__main__":
    ext = get_extension(files)
    create_folder(current_path, ext)
    move_files(files)