import pandas as pd
import requests
import json

 
'Only required at the beginning'
headers = {
    'Authorization': '',
    'accept': 'application/json'
}

'specifying other parameters to search. Basically this can be included in the url'
parameter = {
    'categories': 'restaurants',
    'price':'1,2,3',
    'attributes' : ['parking_street','outdoor_seating']
}

cities = ["bielefeld","hamm","paderborn","essen","dortmund","köln","düsseldorf"]
### If getting business data is your target then check whether the response is positive and work with the data retrieved.
def getbusinesses() -> pd.DataFrame:
    dflist = []
    def getinitialdf():
        try:
            businessurl = f'https://api.yelp.com/v3/businesses/search?location={cities[0]}'
            response = requests.get(url=businessurl, params=parameter, headers=headers)
            if response.status_code == 200:
                try:
                    df = pd.DataFrame(json.loads(response.text)["businesses"])
                    return df
                except:
                    print("dataframe not created.")
        except:
            print("failed request")
    df = getinitialdf()
    for city in cities[1:]:
        businessurl = f'https://api.yelp.com/v3/businesses/search?location={city}'
        response = requests.get(url=businessurl, params=parameter, headers=headers)
        if response.status_code == 200:
            dflist.append(pd.DataFrame(json.loads(response.text)["businesses"]))
        print(f"The request failed due to:{response.text}")
    for dfs in dflist:
        df = pd.concat([df,dfs], ignore_index=True)
    return df

def getbusinessreviews() -> pd.DataFrame: 
    bids,id,review,created_at,rating = [],[],[],[],[]
    businessids = getbusinesses()['id']
    for ids in businessids:
        reviewurl = f'https://api.yelp.com/v3/businesses/{ids}/reviews'
        responsrev = requests.get(url= reviewurl, headers=headers)
        businessidrev = responsrev.json()
        busid = []
        for rev in businessidrev['reviews']:
            id.append(rev['id'])
            review.append(rev['text'])
            created_at.append(rev['time_created'])
            rating.append(rev['rating'])
            busid.append(rev['id'])
        for ele in busid:
            bids.append(ids) 
    return pd.DataFrame({'businessid':bids,'reviewid':id,'review':review,'created_at':created_at,'rating':rating})

#print(getbusinessreviews())