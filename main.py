import sharepoint as sp
from dataextraction import getbusinesses, getbusinessreviews
from exchangerate import get_exchangerate
import postgresops as ps
import logging as lgs


import datetime as dt
import sys
import re


# create logger file with filehandler 'dataingest.log'
lv = lgs.INFO
log = lgs.getLogger(__name__)
#filename = str(dt.date.today()) + ".log"
flg = lgs.FileHandler(filename= str(re.sub("[-:.]+","",str(dt.datetime.now()))) + ".log" , encoding='utf-8')
flg.setLevel(level=lv)
lg_formatter = lgs.Formatter(fmt='%(levelname)s: %(asctime)s %(message)s', datefmt='%d.%m.%y %I:%M:%S')
flg.setFormatter(lg_formatter)
log.addHandler(flg)


def getdata(*argv):
    #*argv is a tuple that contain a single list. This list are enviromental variables
    if argv[0][1] == 'confi':
        data = sp.get_data()  # returns a dictionary of dataframes
        log.info('data retrieved')
        for k,df in data.items():
            df = ps.col2str(df)
            log.info('Starting confidence bakery data ingestion....')
            ps.ingest_data(df=df,schemaname='public', tablename=k)
            log.info('Confidence bakery data successfully ingested!.')
            ps.conn.commit()
            log.info('Now closing database connection.')
            log.info('Database connection closed.')
        log.info(f"Now about to delete data rows from schema:{argv[0][2]} and tables:[{argv[0][3]},{argv[0][4]}].")
        log.info(f'data about to be deleted from schema:{argv[0][2]} and table:{argv[0][3]}.')
        ps.delete_rows(argv[0][2],argv[0][3],argv[0][5])
        log.info(f'data has been deleted from schema:{argv[0][2]} and table:{argv[0][3]}.')
        log.info(f'data about to be deleted from schema:{argv[0][2]} and table:{argv[0][4]}.')
        ps.delete_rows(argv[0][2],argv[0][4],argv[0][5])
        log.info(f'data has been deleted from schema:{argv[0][2]} and table:{argv[0][4]}.')
    elif argv[0][1] == 'yelp':
        log.info('Starting yelp business data ingestion...')
        ps.ingest_data(df= ps.col2str(getbusinesses()), schemaname='public', tablename='yelpbusiness')
        log.info('Yelp Business data successfully ingested!.') 
        ps.conn.commit()
        log.info('Starting yelp business reviews data ingestion...')
        ps.ingest_data(df= ps.col2str(getbusinessreviews()), schemaname='public',tablename='yelbusinessreviews')
        log.info('Starting yelp business reviews data successfully ingested!.')  
        ps.conn.commit()
        log.info('Now closing database connection.')
        log.info('Database connection closed.')
    elif argv[0][1] == 'cfa_exchangerate':
        log.info('Starting central africa franc web scraping and data ingestion...')
        print(get_exchangerate())
        ps.ingest_data(df= ps.col2str(get_exchangerate()), schemaname='public', tablename='cfa_exchangerate')
        log.info('cfa exchange rate data successfully ingested!.') 
        ps.conn.commit()

# if this script is not imported then the __name__ is __main__ otherwise __name__ is name of the script imported
if __name__ == '__main__':
    if len(sys.argv) < 2:
        log.info("Please provide a command-line argument for the script.")
    else:
        log.info("Starting data ingestion...")
        #sys.argv is a list that is passed to getdata. This list becomes a tuple of list because of *argv. *argv is a tuple.
        dt = getdata(sys.argv)
        log.info(f'Now commit and close all connections.')
        ps.conn.commit()
        ps.conn.close()
        

