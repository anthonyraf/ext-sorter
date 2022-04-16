import os
import re

# Current directory complet path
current_path = os.path.dirname(os.path.realpath(__file__))
# Get all files in current directory
files = os.listdir()


# Create ignore file
def create_ignore():
    if not os.path.isfile(current_path + "/ignore.txt"):
        with open(current_path + "/ignore.txt", "w") as f:
            f.write("")


def get_ignored(files):
    ignored = list()
    with open(current_path + "/ignore.txt", "r") as f:
        for i in f.readlines():
            ignored.append(i.strip())
    return ignored

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
            
# TODO: add ignore exceptions
def move_files(files):
    for i in files:  
        ext_ = i.split('.')[-1]
        if os.path.isfile(current_path + "/" + i):
            os.rename(current_path + "/" + i, current_path + "/" + ext_ + "/" + i)

def run():
    create_ignore()
    ext = get_extension(files)
    create_folder(current_path, ext)
    move_files(files)

if __name__ == "__main__":
    run()