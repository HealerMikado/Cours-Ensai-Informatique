class Source:

    SURVEY = "survey"
    CENSUS = "census"
    ADMINISTRATIVE_FILE = "administrative"
    WEBSCRAPPING = "webscrapping" 

    def __init__(self, name, start_collect, end_collect, input_file, type):
        self.name=name
        self.start_collect=start_collect
        self.end_collect=end_collect
        self.input_file=input_file
        self.type=type

    def process(self):
        print ("Traitement de {} avec fichier en entrée {}".format(self.name, self.input_file))
        print ("Date de début de collecte {} ; fin de collecte {}".format(self.start_collect, self.end_collect))
        
        if self.type.lower() == Source.SURVEY:
            print("Traitement d'un fichier d'enquête")
        elif self.type.lower() == Source.CENSUS:
            print("Traitement d'un fichier de recensement")
        elif self.type.lower() == Source.ADMINISTRATIVE_FILE:
            print("Traitement d'un fichier administrative")
        elif self.type.lower() == Source.WEBSCRAPPING:
            print("Traitement d'un fichier de webscrapping")
        else:
            print("foramt de fichier inconnu")
