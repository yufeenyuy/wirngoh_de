import paramiko
import os
import pandas as pd
from io import BytesIO
import datetime as dt
import chardet

import postgresops as ps
from postgresops import to_str, col2str

# Paramiko documentation: https://docs.paramiko.org/en/3.4/api/sftp.html

# SFTP connection detail for connecting to sftp server file storage
sftpurl_host = ''
username = ''
password = ''
port = 22

rootdir = ''
target_folder_or_directory = 'directory where the data is stored on the server'
destination_folder_or_directory = 'directory where the data should go on the server'

# create connection to server and open it.
def openserver():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=sftpurl_host,port=port, username=username,password=password, timeout=10)
    return ssh.open_sftp()

#create sftp client
sftp = openserver()

def getfiles():
    remotefiles = [fii for fii in sftp.listdir(target_folder_or_directory)]
    return remotefiles

confidata = getfiles()

print(confidata)


#def moveto(confidata):
#    for fii in confidata:
#        print(target_folder_or_directory + "/" + fii)
#        sftp.posix_rename(target_folder_or_directory + "/" + fii, destination_folder_or_directory + "/" + fii)
#moveto(confidata=confidata)

#sftp.close()
#openserver().close()
    
def createdf(files = getfiles(),dfs = dict()):
    for file in files:
        if file.endswith('.csv'):
            filepath = os.path.join(target_folder_or_directory,file)
            with sftp.open(filepath,'rb') as opened_remote_file:
                remote_file_content = opened_remote_file.read()
                df = pd.read_csv(BytesIO(remote_file_content), low_memory=False)
                df = col2str(df)
                df.columns = [c.lower() for c in df.columns]
                dfs[file[:-4]] = df
        return dfs

# ingest data into postgresql database. Since the data is large, consider applying chunking in the during ingestion.
ps.ingest_data(createdf()["transport_data"],"fiege","transport_data")


# this segment is for reading data from excel files retrieved from sftp server.
"""
def createdfs(files = getfiles(),dfs = dict()):
    for file in files:
        if file.endswith('.xlsx'):
            filepath = os.path.join(target_folder_or_directory,file)
            open_remote_file = sftp.open(filepath, 'rb')
            remote_file_content = open_remote_file.read()
            df = pd.read_excel(BytesIO(remote_file_content))
            df = col2str(df)
            print(type(df))
            df.columns = [c.lower() for c in df.columns]
            dfs[file] = df
        return dfs
"""





