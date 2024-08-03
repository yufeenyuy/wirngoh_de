import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import ssl


# define ssl to help access https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# I got this header from chatgtp but didn't copy the explanation for its need.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# I need these lists for dataframe creation after scraping the targeted data.
textlis = list()
vallis = list()

def get_exchangerate()-> pd.DataFrame:
    cfa_url = 'https://www.exchangerates.org.uk/Central-African-CFA-franc-XAF-currency-table.html'
    req = urllib.request.Request(url=cfa_url, headers=headers)
    html = urllib.request.urlopen(req, context=ctx).read()
    soup = bs(html, 'html.parser')
    tr = soup.find_all("tr")
    count = 0
    for t  in tr:
        if len(t) == 11:
            # tag.contents puts every contents of this a tag in a python list.
            textlis.append(re.findall("[A-Z ]+",str(t.contents[3]))[0])
            vallis.append(re.findall("[0-9.]+",str(t.contents[7]))[0])
            count = count + 1
    textlis.append("XAF XAF")
    vallis.append("1")
    cfa_exchangrate = pd.DataFrame({"currency" : textlis, "value":vallis})
    cfa_exchangrate["currency"] = cfa_exchangrate["currency"].str.replace("XAF","CFA")
    return cfa_exchangrate