from datetime import datetime

from source.census import Census
from source.survey import Survey
from source.administrative_file import AdministrativeFile
from source.webscrapping import Webscrapping
from file.csv_file import CsvFile
from file.json_file import JsonFile
from file.xml_file import XmlFile

if __name__ == "__main__":

    csv_file_census =  CsvFile("fichier_recensement2020.csv")
    csv_file_survey =  CsvFile("fichier_enquête.csv")
    csv_file_admin =  CsvFile("fichier_admin.csv")

    xml_file_survey = XmlFile("enquête2019.xml")
    xml_file_webscrapping = XmlFile("scrapping_last_night.xml")

    json_file_webscrapping = JsonFile("tweets2019.json")
    json_file_census = JsonFile("recensement_test_json.json")

    sources = [Census("recensement français 2020", datetime(2020,1,1), datetime(2020,12,31), csv_file_census )
    ,Census("recensement test", datetime(2020,1,1), datetime(2020,12,31), json_file_census )
    ,Survey("enquête patrimoine 2018", datetime(2018,3,15), datetime(2018,5,15), csv_file_survey )
    ,Survey("enquête emploi 2019", datetime(2019,3,15), datetime(2019,5,15), xml_file_survey )
    ,AdministrativeFile("DSN_01-2020", datetime(2020,1,1), datetime(2020,1,31), csv_file_admin )
    ,Webscrapping("webscrapping", datetime(2020,1,1), datetime(2020,12,31), xml_file_webscrapping )
    ,Webscrapping("webscrapping_twitter", datetime(2020,1,1), datetime(2020,12,31), json_file_webscrapping )]

    for source in sources :
        source.process()
        print("********")
