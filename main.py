import os


class Sorter:
    def __init__(self):
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.files = os.listdir()
        self.create_ignore()
        self.ignore = self.get_ignored()
        self.ext = self.get_extension(self.files)
        self.create_folder(self.current_path, self.ext)
        self.move_files(self.files)

    def create_ignore(self):
        if not os.path.isfile(self.current_path + "/ignore.txt"):
            with open(self.current_path + "/ignore.txt", "w") as f:
                f.write("")

    def get_ignored(self):
        ignore = list()
        with open(self.current_path + "/ignore.txt", "r") as f:
            for i in f.readlines():
                ignore.append(i.strip())
        return ignore

    def get_extension(self, files):
        ext = list()
        for i in files:
            ext_ = i.split('.')[-1]
            if os.path.isfile(self.current_path + "/" + i):
                if not ext_ in ext:
                    ext.append(ext_)
        return ext

    def create_folder(self, path, ext):
        for i in ext:
            if i not in self.ignore and "."+i.split('.')[-1] not in self.ignore:
                if not os.path.exists(path + "/" + i):
                    os.makedirs(i)

    def move_files(self, files):
        for i in files:
            if i not in self.ignore and "."+i.split('.')[-1] not in self.ignore:
                ext_ = i.split('.')[-1]
                if os.path.isfile(self.current_path + "/" + i):
                    os.rename(self.current_path + "/" + i,
                              self.current_path + "/" + ext_ + "/" + i)

Sorter()