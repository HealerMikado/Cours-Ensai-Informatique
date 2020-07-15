from abc import ABC, abstractmethod

class AbstractFile(ABC):
    def __init__(self, path) :
        self.path = path

    @abstractmethod
    def parse(self):
        pass