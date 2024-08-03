import requests
import pandas as pd
import os
from adal import AuthenticationContext
import datetime as dt
import io

# Azure AD App Registration Details
client_id = ""
client_secret = ""
tenant_id = ""
authority_url = f"https://login.microsoftonline.com/{tenant_id}"
resource_url = "https://graph.microsoft.com"
site_name = ""
folder_name = "data"
siteurl = ""

#This is an alternative way to retrieve the bearer or access token. It uses the authenticationcontext method from the adal library.
def get_bearer_token(authority_url,resource_url, client_id, client_secret) -> str:
    context = AuthenticationContext(authority = authority_url)
    token = context.acquire_token_with_client_credentials(resource_url,client_id= client_id, client_secret= client_secret)
    return token['accessToken']

myaccestoken = get_bearer_token(authority_url, resource_url,client_id,client_secret)


def get_access_token(tenantid, clientid, clientsecret) -> str:
    token_url = f"https://login.microsoftonline.com/{tenantid}/oauth2/token"
    token_data = {
        "grant_type": "client_credentials",
        "client_id": clientid,
        "client_secret": clientsecret,
        "resource": "https://graph.microsoft.com"
    }
    token_response = requests.post(token_url, data=token_data)
    token = token_response.json().get("access_token")
    return token

print(get_access_token(tenantid=tenant_id,clientid=client_id,clientsecret=client_secret))

def get_site_id(sitename, tenantid, clientid, clientsecret) -> str:
        bearer_token = get_access_token(tenantid,clientid,clientsecret)
    # Use the access token to retrieve site information
        headers = {
            "Authorization": f"Bearer {bearer_token}",
        }
        site_url = f"https://graph.microsoft.com/v1.0/sites?search={sitename}"

        response = requests.get(site_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print('this data:',data)
            if 'value' in data and len(data['value']) > 0:
                site_id = data['value'][0]['id']
                return bearer_token, site_id
            else:
                print(f"Site '{site_name}' not found.")
        else:
            print("Failed to retrieve site information.")
        return None

#print(get_site_id(sitename=site_name,tenantid=tenant_id,clientid=client_id,clientsecret=client_secret))


def get_folder_id(folderpath,sitename,tenantid,clientid,clientsecret) -> str:
    token_and_id =  list(get_site_id(sitename, tenantid,clientid,clientsecret))
    access_token =  token_and_id[0]
    site_id =  token_and_id[1]
    graph_path = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/{folderpath}"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(graph_path, headers= headers)
    if response.status_code == 200:
        folder_metadata = response.json()
        folder_item_id = folder_metadata["id"]
        return access_token,site_id,folder_item_id
    else:
        print(f"Failed to retrieve folder metadata. Status code: {response.status_code}")
        return None
    
data_folder_item_id = get_folder_id(folder_name,site_name,tenant_id,client_id,client_secret)


def get_files() -> list:
    files = list()
    graph_url = f"https://graph.microsoft.com/v1.0/sites/{data_folder_item_id[1]}/drive/items/{data_folder_item_id[2]}/children"
    headers = {
            "Authorization": f"Bearer {data_folder_item_id[0]}"
        }
    response = requests.get(graph_url, headers=headers)
    #print(response.text)
    if response.status_code == 200:
        data = response.json()
        for child in data['value']:
            # Check if it's a file (you can customize the logic here)
            if 'file' in child:
                file_name = child['name']
                file_id = child['id']
                #print(file_name)
                files.append(file_name)
                # Process the file as needed
    else:
        print(f"Failed to list children in the 'data' folder. Status code: {response.status_code}")
    return files


def get_data(datafiles = dict()) -> dict:
    # Get the list of files from SharePoint folder
    files = get_files()
    for file_name in files:
        # Check if the file is an Excel file (you can customize the logic here)
        if file_name.__contains__('20230826'):
            sheetnames = ['Production_Data', 'Sales_Data']
            # Construct the URL for the Excel file
            excel_file_url = f"https://graph.microsoft.com/v1.0/sites/{data_folder_item_id[1]}/drive/items/{data_folder_item_id[2]}/children/{file_name}/content"

            # Set the authorization header
            headers = {
                "Authorization": f"Bearer {data_folder_item_id[0]}"
            }
            # Send a GET request to download the Excel file
            response = requests.get(excel_file_url, headers=headers)
            if response.status_code == 200:
                for name in sheetnames:
                    # Read the Excel file into a pandas dataframe
                    excel_data = pd.read_excel(io.BytesIO(response.content), sheet_name=name)
                    datafiles[name.lower()] = excel_data
                print(f"Successfully read data from '{file_name}'.")
            else:
                print(f"Failed to download '{file_name}'. Status code: {response.status_code}")

    return datafiles

get_data()

# Now 'excel_dataframes' is a list containing pandas dataframes for each Excel file
# You can access individual dataframes using indexing, e.g., excel_dataframes[0], excel_dataframes[1], etc.
#this is what i did to get the folder id. I pushed the result in chatgpt and i got the item-id for the target folder.
#In fact this is how to get the metadata of an item-path or folder. If the response of the request is valid, then
#you can get the item-id or identifier of the folder from the metadata of the the folder.
#graph_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/data"
# Construct the request URL to list children of the "data" folder. Note that the item-id is simply the id or identifier of a folder!
#data_folder_item_id = '01UH3M5BKNQ5DWZDFVCFF2RIO4X3Q55E2J'
# once the item-id for the target folder was retrieved by chatgpt, it is then used to get the files(children) in this folder
#graph_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/items/{data_folder_item_id}/children"


