class Source(object):
    def __init__(self, name, start_collect, end_collect,input_file):
        self.name=name
        self.start_collect=start_collect
        self.end_collect=end_collect
        self.input_file=input_file

    def common_process(self):
        print ("Traitement de {} avec fichier en entrée {}".format(self.name, self.input_file))
        print ("Date de début de collecte {} ; fin de collecte {}".format(self.start_collect, self.end_collect))

    def custom_process(self):
        raise NotImplementedError
        
    def process(self):
        self.common_process()
        self.custom_process()