import os

# Current directory complet path
current_path = os.path.dirname(os.path.realpath(__file__))
files = os.listdir()
ext = list()

def get_extension(files):
    for i in files:
        ext_ = i.split('.')[-1]
        if os.path.isfile(current_path + "/" + i):
            if not ext_ in ext:
                ext.append(ext_)

def create_folder(path):
    for i in ext:
        if not os.path.exists(path + "/" + i):
            os.makedirs(i)

#  TODO : Create a function to move files to their respective folders
def move_files():
    for i in ext:
        os.

