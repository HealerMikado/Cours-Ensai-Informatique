from abc import ABC, abstractmethod

class AbstractSource(ABC):
    def __init__(self, name, start_collect, end_collect,input_file):
        self.name=name
        self.start_collect=start_collect
        self.end_collect=end_collect
        self.input_file=input_file


    def common_process(self):
        self.input_file.parse()
        print ("Date de début de collecte {} ; fin de collecte {}".format(self.start_collect, self.end_collect))


    @abstractmethod
    def custom_process(self):
        pass


    def process(self):
        self.common_process()
        self.custom_process()