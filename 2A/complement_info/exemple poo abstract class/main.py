from datetime import datetime

from census import Census
from survey import Survey
from administrative_file import AdministrativeFile
from webscrapping import Webscrapping

if __name__ == "__main__":
    sources = [Census("recensement français 2020", datetime(2020,1,1), datetime(2020,12,31), "recensement_2020.txt" )
    ,Survey("enquête patrimoine 2018", datetime(2018,3,15), datetime(2018,5,15), "patrimoine2018.txt" )
    ,AdministrativeFile("DSN_01-2020", datetime(2020,1,1), datetime(2020,1,31), "dsn_01_2020.txt" )
    ,Webscrapping("webscrapping_twitter", datetime(2020,1,1), datetime(2020,12,31), "tw2020.txt" )]

    for source in sources :
        source.process()
        print("********")
        # tester le code en commentant une des méthodes custom_process().
        #  Que ce passe-t-il ? 
        # Bon comportement d'après vous ?