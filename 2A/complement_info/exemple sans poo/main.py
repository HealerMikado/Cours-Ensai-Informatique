from datetime import datetime

from source import Source

if __name__ == "__main__":
    sources = [Source("recensement français 2020", datetime(2020,1,1), datetime(2020,12,31), "recensement_2020.txt", Source.CENSUS )
    ,Source("enquête patrimoine 2018", datetime(2018,3,15), datetime(2018,5,15), "patrimoine2018.txt", Source.SURVEY )
    ,Source("DSN_01-2020", datetime(2020,1,1), datetime(2020,1,31), "dsn_01_2020.txt", Source.ADMINISTRATIVE_FILE )
    ,Source("webscrapping_twitter", datetime(2020,1,1), datetime(2020,12,31), "tw2020.txt", Source.WEBSCRAPPING )]

    for source in sources :
        source.process()
        print("********")

