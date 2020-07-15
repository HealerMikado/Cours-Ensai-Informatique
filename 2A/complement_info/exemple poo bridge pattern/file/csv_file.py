from  file.abstract_file import AbstractFile

class CsvFile(AbstractFile):
    def __init__(self, path):
        super().__init__(path)

    def parse(self):
        
        print("Parse le fichier {} qui est un fichier csv".format(self.path))
        