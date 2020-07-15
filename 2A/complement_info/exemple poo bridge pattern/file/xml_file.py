from  file.abstract_file import AbstractFile

class XmlFile(AbstractFile):
    def __init__(self, path):
        super().__init__(path)

    def parse(self):
        print("Parse le fichier {} qui est un fichier xml".format(self.path))
        