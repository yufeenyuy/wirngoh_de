import psycopg2 as ps
from sqlalchemy import create_engine
import datetime as dt
import pandas as pd
import logging as lg


lg.basicConfig(filename='dataingest.log', encoding='utf-8', format='%(levelname)s: %(asctime)s %(message)s.', datefmt='%d.%m.%Y %I:%M:%S', level=lg.DEBUG)

#convert data types of pandas dataframe to strings
def to_str(df):
    df['loaded_at'] = dt.datetime.now()
    df = map(lambda x: str(x),df)
    return df
#Alternative function used to convert data types of a pandas dataframe to strings.
def col2str(df):
    df['loaded_at'] = dt.datetime.now()
    df = df.applymap(str)
    return df

#use a dataframe df2 to update records of another dataframe df1 by a key column.
def updatedf(df1, df2):
    df1.set_index(df1.iloc[:,0], inplace = True)
    df2.set_index(df2.iloc[:,0], inplace = True)
    df1.update(df2)
    return df1


user = ''
db_name = ''
host = ''
port = 5432
password = ''

conn = ps.connect(host = host, port = port,dbname = db_name, user = user, password = password)

connstr = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'

engine = create_engine(connstr)

cur = conn.cursor()

#check whether schema or table exist.
def checkschema_and_table(schemaname,tablename):
    q1 = """select exists(select schema_name from information_schema.schemata where schema_name = %s)"""
    cur.execute(q1,(schemaname,))
    result = cur.fetchone()[0]
    def checktable(tablename):
        q2 = """select exists(select table_name from information_schema.tables where table_name = %s)"""
        cur.execute(q2,(tablename,))
        result = cur.fetchone()[0]
        return result
    return result,checktable(tablename)

#Delete rows from table that are earlier that 5 day
def delete_rows(schemaname, tablename, tablecol) -> None:
    result = checkschema_and_table(schemaname,tablename)
    print(result)
    if result[0] and result[1]:
        q3 = f"""delete from {schemaname}.{tablename} where {tablecol}::date <= current_date - interval '5 days'"""
        cur.execute(q3)
        conn.commit()
    return None

#This function applies only on datasets that should be ingested once.
def ingest_data(df,schemaname, tablename):
    result = checkschema_and_table(schemaname,tablename)
    if result[1] is True:
        lg.info(f'Schema:{schemaname} and table:{tablename} exist in the database so table:{tablename} will be appended to existing one.')
        df.to_sql(tablename, con=engine,if_exists = 'append',index=False, schema= schemaname)
    elif result[0] is True and result[1] is False:
        lg.info(f'Target Schema:{schemaname} but table:{tablename} does not exist so table:{tablename} will be ingested into Schema:{schemaname}.')
        df.to_sql(tablename, con=engine,index=False, schema= schemaname)
        lg.info(f'{tablename} has been ingested in schema:{schemaname}')
    return




