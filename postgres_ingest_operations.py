import psycopg2 as ps
from sqlalchemy import create_engine, update, select,insert, MetaData, Table, inspect, and_, exists
from sqlalchemy.dialects.postgresql import insert
import datetime as dt
import pandas as pd

host = ''   #'dapostgres.postgres.database.azure.com'
port = 5432
dbname = ''
dbuser = ''
password = ''

#conn = ps.connect(host = 'localhost', port = 5432,dbname = 'postgres', user = 'postgres', password = 'Nyuysemo1,')
conn = ps.connect(host = host, port = port, dbname = dbname , user = dbuser , password = password)


# Create a database engine
connstr = f'postgresql+psycopg2://{dbuser}:{password}@{host}:{port}/{dbname}'

engine = create_engine(connstr)

cur = conn.cursor()

target = pd.DataFrame(data={'id':[1,2,3,4,5],
                      'name':['Senyuy','Sahnyuy','Wanyu','Dinnyuy','Limnyuy'],
                      'age':[23,36,71,26,42]})

target['refresh'] = dt.date.today()

new_data = pd.DataFrame(data={'id':[2,3,5,6],
                      'name':['Leinyuy','Tanlaka','Dzesinyuy','Lemnyuy'],
                      'age':[63,34,28,10]})
new_data['refresh'] = dt.date.today()


'''Use pandas update function to update df1 with df2 under assumption that the first column of each of these dfs have unique values'''
#This method is recommended for cases when the data is not yet existent in the database.

def updatedf(df1, df2):
    df1.set_index(df1.iloc[:,0], inplace = True)
    df2.set_index(df2.iloc[:,0], inplace = True)
    df1.update(df2)
    return df1

schema_name = 'fakedata'

cur.execute(f'''CREATE SCHEMA IF NOT EXISTS {schema_name}''')
conn.commit()

target.to_sql('target', con=engine, if_exists='replace', index=False,schema=schema_name)

new_data.to_sql('source', con=engine, if_exists='replace', index=False,schema=schema_name)

target.to_sql('target_persons', con=engine, if_exists='replace', index=False,schema=schema_name)

target.to_sql('targets', con=engine, if_exists='replace', index=False,schema=schema_name)

new_data.to_sql('sources', con=engine, if_exists='replace', index=False,schema=schema_name)

conn.commit()

"""
#set a column of a database table as the primary key.
def set_pkey(schemaname, tablename, tablecol):
    alterq = f'''ALTER TABLE {schemaname}.{tablename} ADD PRIMARY KEY ({tablecol})'''
    cur.execute(alterq)
    conn.commit()
    return None

set_pkey(schema_name,'targets','id')
set_pkey(schema_name,'sources','id')

conn.commit()

def has_primary_key(schema, tablename):
    # Reflect the database schema
    meta = MetaData()
    meta.reflect(bind=engine, schema=schema)

    # Get the table object
    tabele = Table(tablename,meta, autoload_with=engine, autoload = True, schema=schema)
    #table_colnames = [col.name for col in tabele.columns]

    inspector = inspect(engine)
    primary_keys = inspector.get_pk_constraint(table_name=tablename, schema=schema)
    return bool(primary_keys.get('constrained_columns'))

# Usage example
table_name = 'targets'
result = has_primary_key(schema_name, table_name)
print(f'Table {table_name} in schema {schema_name} has a primary key: {result}')

#check existence of table in database
def checktable(schema, tablename):
    query = '''SELECT EXISTS(SELECT 1 FROM 
    information_schema.tables where
    table_schema = %s AND table_name = %s)'''
    cur.execute(query,(schema,tablename))
    result = cur.fetchone()[0]
    return result

checktable(schema_name,'target')
checktable(schema_name,'source')

#check existing table in database on emptyness
def tablezize(schemaname,tablename) -> int:
    query = f'select count(*) from {schemaname}.{tablename}'
    cur.execute(query)
    result = cur.fetchone()[0]
    print(f'Then number of rows in {tablename} is: {result}')
    return result

print('Nunber of rows: ',tablezize(schema_name,'target'))
print('Number of rows: ',tablezize(schema_name,'source'))


# Existing source and target tables in database have a column with unique values but it is not a primary key.
def dynupdate(schemaname, targettable, sourcetable) -> None:
    metainfo = MetaData()
    metainfo.reflect(bind=engine, schema=schemaname)

    if f'{schemaname}.{targettable}' not in metainfo.tables:
        raise ValueError(f'Table "{targettable}" not found in schema "{schemaname}')
    
    target_table = Table(targettable, metainfo, autoload = True, autoload_with=engine,schema=schema_name)

    target_columns = [column.name for column in target_table.columns]

    if f'{schemaname}.{sourcetable}' not in metainfo.tables:
        raise ValueError(f'Table "{sourcetable}" not found in schema "{schemaname}')
    
    source_table = metainfo.tables[f'{schemaname}.{sourcetable}']

    update_cols = {}
    for col_name in target_columns:
        if col_name != 'id':  
            update_cols[col_name] = getattr(source_table.c, col_name)
    
    updateq = update(target_table).values(**update_cols).where(
        target_table.c.id == source_table.c.id
    )

    with engine.begin() as conn:
        try:
            conn.execute(updateq)
            conn.commit()
        except Exception as e:
            print(f'An error occured: {str(e)}')
    
    return None

#dynupdate(schemaname=schema_name, targettable='target', sourcetable='source')

#update database table with incoming dataframe. target = Table with primary key in DB, source = incoming dataframe with new data.
def dynupdate_key(schemaname,targettable,df):
    metainfo = MetaData()
    metainfo.reflect(bind=engine,schema=schemaname)

    target_table = Table(targettable,metainfo,autoload = True, autoload_with=engine, schema=schemaname)

    targetted = pd.read_sql_table(table_name=targettable, con=engine, schema=schemaname)

    df_new = pd.merge(df,targetted, how='inner', on='id')

    df_col = df.columns.tolist()
    df_ncol = len(df_col)
    df_new = df_new.iloc[:,:df_ncol]
    df_new.columns = df_col

    df_dict = df_new.to_dict(orient='records')

    with engine.begin() as conn:
        for dt_row in df_dict:
            filter_records = (target_table.c['id'] == dt_row['id'])
            up_stmt = update(target_table).values(df_dict).where(filter_records)
            conn.execute(up_stmt)
        conn.commit()
    return

#dynupdate_key(schemaname= schema_name,targettable= 'targets',df= new_data)

#upsert: On conflict do update or insert only.Note that the existing tables in the database have no defined primary key but have a column with unique values.
def dynupsert(schemaname, targettable, sourcetable, upserttype):
    metainfo = MetaData()
    metainfo.reflect(bind=engine, schema=schemaname)
    
    if f'{schemaname}.{targettable}' not in metainfo.tables:
        raise ValueError(f'Table "{targettable}" not found in schema "{schemaname}"')
    
    target_table = Table(targettable, metainfo, autoload=True, autoload_with=engine, schema=schemaname)
    target_columns = [column.name for column in target_table.columns]

    if f'{schemaname}.{sourcetable}' not in metainfo.tables:
        raise ValueError(f'Table "{sourcetable}" not found in schema "{schemaname}"')
    
    source_table = Table(sourcetable, metainfo, autoload=True, autoload_with=engine, schema=schemaname)
    select_query = select(source_table)
    
    #select all values in the source table that are not in the target table
    subquery = select(source_table).where(source_table.c.id == target_table.c.id) #wherecriteria
    condition = ~exists(subquery)  #negate the wherecriteria i.e retain source values not in target table
    stmt = select_query.where(condition) #use where criteria as condition in the select where clause.

    update_columns = {}
    for column_name in target_columns:
        if column_name != 'id':  # Skip updating the primary key column
            update_columns[column_name] = getattr(source_table.c, column_name)
    
    update_query = update(target_table).values(**update_columns).where(
        target_table.c.id == source_table.c.id
    )
    
    with engine.begin() as conn:
        result = conn.execute(stmt)
        if upserttype == 'insert':
            for row in result:
                insert_stmt = insert(target_table).values(row)
                conn.execute(insert_stmt)
                conn.commit()

        #mimic upsert method
        else:
            conn.execute(update_query)
            for row in result:
                print("row to insert:", row)
                insert_stmt = insert(target_table).values(row)
                conn.execute(insert_stmt)
            conn.commit()    
    return None


#dynupsert(schemaname=schema_name,targettable='target_persons',sourcetable='source', upserttype='insert_on_conflict')

#upsert: update + insert values from dataframe in a database table that has a primary key.
def dynupsert_update_on_conflict(schemaname, targettable, df) -> None:
    metainfo = MetaData()
    metainfo.reflect(bind=engine, schema=schemaname)

    if f'{schemaname}.{targettable}' not in metainfo.tables:
        raise ValueError(f'Table "{targettable}" not found in schema "{schemaname}')
    
    target_table = Table(targettable, metainfo, autoload = True, autoload_with=engine,schema=schema_name)

    target_columns = [column.name for column in target_table.columns]

    df_dict = df.to_dict(orient = 'records')

    upsert_stmt = insert(target_table).values(df_dict).on_conflict_do_update(
        index_elements = target_table.primary_key,    #This will also work: [col for col in target_columns if col == 'id'],
        set_ = {col: insert(target_table).values(df_dict).excluded[col] for col in target_columns if col != 'id'}
    )
    with engine.begin() as conn:
        try:
            conn.execute(upsert_stmt)
            conn.commit()
        except Exception as e:
            print(f'An error occured: {str(e)}')
    
    return None

def append(df,schemaname, tablename):
    df.to_sql(tablename, con=engine, if_exists='append', index=False,schema=schemaname)
"""