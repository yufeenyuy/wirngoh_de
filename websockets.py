"""Using Tranport Control Protocol (TCP) to enable computers(Client-Server) communicate with each other accross the internet.
Usually a Server host serveral applications. Every application on the server has a unique port associated to it. Whenever a Client
wants to communicate with a particular application, a connection to this application must first be established 
through its port. It is through this port that the server receives client requests, processes them then sends back results to the client.
In summary a server contains applications and ports."""

import socket as sk

# This creates a client
sket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

# This establishes a connection to an application(web server),via the transport layer,on the server/host(data.pr4e.org).Web Server has a port of 80.
"If the connection fails then the server does not exist."
sket.connect(('data.pr4e.org',80))

# Now that the connection has been established, request can now be made to get data. This occurs in the application layer.
"""The Protocol we'll use in this application layer to retrieve data from the web server is HTTP: Hypertext Transfer Protocol.
Using this protocol we can make get and send requests to the web server."""

# Making a get request.
'''first of all set the request to be made. 
Notice that the request has \n\n. This means the request should end at the end of the line and followed by a blank space.
The blank space is necessary because the web server returns data in two portions.
The first portion is the meta data while the second portion is the content we actually need.
It is important to note that every request sent by the client to the server over the internet is encoded i.e in bytes.
It is recommended to encode the request in utf-8'''
request = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

'''Then send the request. This is where data is retrieved from the web server. This request means that 
go to the web server data.pr4e.org and get the data in http://data.pr4e.org/romeo.txt'''
sket.send(request)

'Check content of the request returned from the web server.'
while True:
    data = sket.recv(510)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
sket.close()


#########################################################################################################################################
"using urllib library to send requests to web server."
"using urllib library to send requests to web server."
import urllib.request, urllib.parse, urllib.error
import re

"""This call implements the sockets functions upto the *send* under the hood. urlopen operates like open used in opening files.
Remember that this request is encoded.
"""
url1 = 'http://data.pr4e.org/romeo.txt'
url = 'https://data.pr4e.org/romeo-full.txt'

fandl = urllib.request.urlopen(url=url1)
fhand = urllib.request.urlopen(url=url)

# create a list of strings where these strings are lines.
linelist = fhand.read().decode().splitlines()


counts = dict()
wordlist = list()
for line in linelist:
    "split every line in the list into words"
    words = line.split()
    if len(words) < 1: pass
    else:
        print("words in list",words)
        for word in words:
            wordlist.append(re.sub("[-?/!$&;',.]",'',word.lower()))
        for word in wordlist:
            counts[word] = counts.get(word, 0) + 1
print(counts)

# create a list of words
newcounts = dict()
newwordlist = list()
fhandl = fandl.read().decode().split()
for word in fhandl:
    newwordlist.append(re.sub("[-?.,;$&/!]",'',word.lower()))

for newword in newwordlist:
    newcounts[newword] = newcounts.get(newword,0) + 1
print(newcounts)


#########################################################################################################################################
'''Web scraping:
The use of a program or script(e.g python script) to mimic the action of a browser and retrieve data from a web server.'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import ssl

# define ssl to help access https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE 

# Assignment 1 #
# define the url from which data needs to be scraped
comments_1982232 = 'https://py4e-data.dr-chuck.net/comments_1982232.html'

# read the entire content into a single where lines are separated by line breakers.
'The response of this request is very unstructured as it pull the content of the url as it is developed in the backend.'
html = urllib.request.urlopen(url=comments_1982232, context=ctx).read()

# Use BeautifulSoup to organise the response from the web server into a tree.
'Think of this as organising the content of web page hierarchichally i.e from the top to the lowest hierarchy.'
soup = bs(html, 'html.parser')

span = soup.find_all('span')

current_val = 0
for sp in span:
    current_val = current_val + int(sp.text)
#print(current_val)

# Assignment 2 #

link = 'http://py4e-data.dr-chuck.net/known_by_Lancelot.html'

def getname(link):
    html_request = urllib.request.urlopen(url=link,context=ctx).read()
    soup_a2 = bs(html_request,'html.parser')
    a2_anchors = soup_a2.find_all('a')
    anchor_links = list()
    for ele in a2_anchors:
        anchor_links.append(ele.get('href', None))
    return anchor_links[17]

for i in range(9):
    newlink = getname(link)
    print(link)
    link = newlink

#Below is how data can be retrieved from an anchor tag
'''
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None) gets link or url in an anchor tag
   print 'Contents:',tag.contents[0]  gets the content of an anchor tag
   print 'Attrs:',tag.attrs      get the value of an attribute in an anchor tag
'''

##################################################################################################################################
# working with xlm
import xml.etree.ElementTree as ET

# create xml for serialization
data = '''
      <Town>
          <Zipcodes>
              <Zipcode zip = "1111">
                  <Streets>
                      <Street>
                           Kishi
                           <Housenumbers Housenr="[1,2,3,4,5,6,7,8]" /> 
                      </Street>
                      <Street>
                           Kovwong
                           <Housenumbers Housenr="[9,10,11,12,13,14,15,16]" />
                      </Street>
                      <Street>
                           Wiryihlo jaikinyo
                           <Housenumbers Housenr="[17,18,19,20,21,22,23,24]" />
                      </Street>
                      <Street>
                           Ntohti
                           <Housenumbers Housenr="[25,26,27,27,28,29,30,31]" />
                      </Street>
                      <Street>
                           Mbuluf
                           <Housenumbers Housenr="[32,33,34,35,35,36,37,38]" />
                      </Street>
                  </Streets>
              </Zipcode>
              <Zipcode zip = "1110">
                  <Streets>
                      <Street>
                           Tahtum
                           <Housenumbers Housenr="[1,2,3,4,5,6,7,8]" />
                      </Street>
                      <Street>
                           Mantum
                           <Housenumbers Housenr="[9,10,11,12,13,14,15,16]" />
                      </Street>
                      <Street>
                           Tan
                           <Housenumbers Housenr="[17,18,19,20,21,22,23,24]" />
                      </Street>
                      <Street>
                           Shi
                           <Housenumbers Housenr="[25,26,27,27,28,29,30,31]"/>
                      </Street>
                      <Street>
                           Mbokam
                           <Housenumbers Housenr="[32,33,34,35,35,36,37,38]" />
                      </Street>
                  </Streets>
              </Zipcode>
              <Zipcode zip = "1101">
                  <Streets>
                      <Street>
                           Ber
                           <Housenumbers Housenr="[1,2,3,4,5,6,7,8]" />
                      </Street>
                      <Street>
                           Waihnamah
                           <Housenumbers Housenr="[9,10,11,12,13,14,15,16]" />
                      </Street>
                      <Street>
                           Nkar
                           <Housenumbers Housenr="[17,18,19,20,21,22,23,24]" />
                      </Street>
                      <Street>
                           Sop
                           <Housenumbers Housenr="[25,26,27,27,28,29,30,31]"/>
                      </Street>
                      <Street>
                           Kikaikelahki
                           <Housenumbers Housenr="[32,33,34,35,35,36,37,38]" />
                      </Street>
                  </Streets>
              </Zipcode>
              <Zipcode zip = "1011">
                  <Streets>
                      <Street>
                           Kikaikom
                           <Housenumbers Housenr="[1,2,3,4,5,6,7,8]" />
                      </Street>
                      <Street>
                           Kinsenjam
                           <Housenumbers Housenr="[9,10,11,12,13,14,15,16]" />
                      </Street>
                      <Street>
                           Vekovi
                           <Housenumbers Housenr="[17,18,19,20,21,22,23,24]" />
                      </Street>
                      <Street>
                           Melim
                           <Housenumbers Housenr="[25,26,27,27,28,29,30,31]" />
                      </Street>
                      <Street>
                           Kimar
                           <Housenumbers Housenr="[32,33,34,35,35,36,37,38]" />
                      </Street>
                  </Streets>
              </Zipcode>
              <Zipcode zip = "1111">
                  <Streets>
                      <Street>
                           Rontong
                           <Housenumbers Housenr="[1,2,3,4,5,6,7,8]" />
                      </Street>
                      <Street>
                           Kiluun
                           <Housenumbers Housenr="[9,10,11,12,13,14,15,16]" />
                      </Street>
                      <Street>
                           Mensay
                           <Housenumbers Housenr="[17,18,19,20,21,22,23,24]" />
                      </Street>
                      <Street>
                           Shishong
                           <Housenumbers Housenr="[25,26,27,27,28,29,30,31]" />
                      </Street>
                      <Street>
                           Shangwai
                           <Housenumbers Housenr="[32,33,34,35,35,36,37,38]" />
                      </Street>
                  </Streets>
              </Zipcode>
              <Zipcode zip = "1001">
                  <Streets>
                      <Street>
                           Kifem
                           <Housenumbers Housenr="[1,2,3,4,5,6,7,8]" />
                      </Street>
                      <Street>
                           Tobin
                           <Housenumbers Housenr="[9,10,11,12,13,14,15,16]" />
                      </Street>
                      <Street>
                           Yei
                           <Housenumbers Housenr="[17,18,19,20,21,22,23,24]" />
                      </Street>
                      <Street>
                           Nseni
                           <Housenumbers Housenr="[25,26,27,27,28,29,30,31]" />
                      </Street>
                      <Street>
                           Mbonso
                           <Housenumbers Housenr="[32,33,34,35,35,36,37,38]" />
                      </Street>
                  </Streets>
              </Zipcode>
              <Zipcode zip = "1100">
                  <Streets>
                      <Street>
                           Meluf
                           <Housenumbers Housenr="[1,2,3,4,5,6,7,8]" />
                      </Street>
                      <Street>
                           Kitiwum
                           <Housenumbers Housenr="[9,10,11,12,13,14,15,16]" />
                      </Street>
                      <Street>
                           Kiyang
                           <Housenumbers Housenr="[17,18,19,20,21,22,23,24]" />
                      </Street>
                      <Street>
                           Tadu
                           <Housenumbers Housenr="[25,26,27,27,28,29,30,31]" />
                      </Street>
                      <Street>
                           Mbiame
                           <Housenumbers Housenr="[32,33,34,35,35,36,37,38]" />
                      </Street>
                  </Streets>
              </Zipcode>
          </Zipcodes>
      </Town>
'''

# convert xml to a tree
tree = ET.fromstring(data)

# get zipcodes
zipcodes = tree.findall('Zipcodes/Zipcode')

all_zipcodes = [zip.get('zip').strip() for zip in zipcodes]
print(all_zipcodes)

# parse path to get all streets in the tree.
streets = tree.findall('Zipcodes/Zipcode/Streets/Street')

# store streets in a list using list comprehension.
all_streets = [street.text.strip() for street in streets]
print(all_streets)

# Get house numbers
housenumbers = tree.findall('Zipcodes/Zipcode/Streets/Street/Housenumbers')

all_housenumbers = [houses.get('Housenr').strip() for houses in housenumbers]
print(all_housenumbers)

for hurs in all_housenumbers:
    listele = hurs.strip()
    print(listele,len(listele))

# Assignment 3
comments_42 = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_1982234.xml').read()


comments_tree = ET.fromstring(comments_42).findall('comments/comment')

counts = 0

comments_count = [ele.find('count').text.strip() for ele in comments_tree]

print(comments_count)

for count in comments_count:
    counts = counts + int(count)

print(counts)

#### Working with json files. JSON mean javascript object notation. JSON is also used for information serialization like xml.

import json

json_data = '''{
            "Families" : {
                        "Yuveyonge" : {
                                    "Father" : {
                                             "First Name" : "Yuveyonge",
                                             "Last Name" : "Shutahka",
                                             "Age" : "43",
                                             "Marital Status" : "Married",
                                             "Previously Married" : "True",
                                             "Number of Children" : "3"
                                             },
                                    "Mother" : {
                                            "Last Name" : "Sevidzem",
                                            "First Name" : "Dula",
                                            "Age" : "38",
                                            "Marital Status" : "Married",
                                            "Previously Married" : "False",
                                            "Number of Children" : "3"
                                            },
                                    "First Child" : {
                                            "Last Name" : "Bermo",
                                            "First Name" : "Yula",
                                            "Age" : "17",
                                            "Marital Status" : "Single",
                                            "Previously Married" : "False",
                                            "Number of Children" : "0"
                                            },
                                    "Second Child" : {
                                            "Last Name" : "Nyuysemo",
                                            "First Name" : "Kininla",
                                            "Age" : "13",
                                            "Marital Status" : "Single",
                                            "Previously Married" : "False",
                                            "Number of Children" : "0"
                                            },
                                    "Third Child" : {
                                            "Last Name" : "Dzelamonyuy",
                                            "First Name" : "Kisifey",
                                            "Age" : "8",
                                            "Marital Status" : "single",
                                            "Previously Married" : "False",
                                            "Number of Children" : "0"
                                            }
                                   },
                         "Ayuni" : {
                                   "Father" : {
                                            "Last Name" : "Ayuni",
                                            "First Name" : "Kolem",
                                            "Age" : "36",
                                            "Marital Status" : "Married",
                                            "Previously Married" : "False",
                                            "Number of Children" : "2"
                                            },
                                   "Mother" : {
                                            "Last Name" : "Nyuyleiyi",
                                            "First Name" : "Sikem",
                                            "Age" : "30",
                                            "Marital Status" : "Married",
                                            "Previously Married" : "False",
                                            "Number of Children" : "2"
                                            },
                                   "First Child" : {
                                            "Last Name" : "Dzekem",
                                            "First Name" : "Viban",
                                            "Age" : "10",
                                            "Marital Status" : "Single",
                                            "Previously Married" : "False",
                                            "Number of Children" : "0"
                                            },
                                   "Second Child" : {
                                            "Last Name" : "Dzelafen",
                                            "First Name" : "Nyuyleimo",
                                            "Age" : "7",
                                            "Marital Status" : "Single",
                                            "Previously Married" : "False",
                                            "Number of Children" : "0"
                                            }
                                   }
                        }
            }
'''
# Transform the json into a python dictionary.
load_json = json.loads(json_data)

# Get information about a particular family e.g Ayuni
print(load_json["Families"]["Ayuni"])

# create a list of tuples using list comprehension. Remember that tuples are immutable. .items() returns tuples
families = [ke for ke in load_json["Families"].items()]

# Get mothers information
for family in families:
    if "Mother" in family[1].keys():
        print(f'The Mothers details for the family: {family[0]} are {family[1]["Mother"]}')

# Get the sum of all the nunber of children in the families.
'''Since every member of the family has the variable "Number of Children". Let's assume they all Father and mother have same number of 
children as they are parents. Let's also assume children have different number of children as well.'''
"Let's create a set containing unique values for number of children every member of the family has."
numberofchildren = set()
for family in families:
    for key, val in family[1].items():
        numberofchildren.add(int(val["Number of Children"]))
print(f"The total number of children is {sum(numberofchildren)}")


# Assignment 3 on reading data from json

json_comments_42 = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_1982235.json').read()

a3_comments = json.loads(json_comments_42)

json_comment_counts = list()

for dicts in a3_comments["comments"]:
    json_comment_counts.append(int(dicts["count"]))
print(sum(json_comment_counts))

# Service oriented approach
"""This is a approach that allows a System to share its services with one or more other Systems based on an agreed contract or rules.
This approach is implemented using APIS (Application Programing Interface) which is a way to use web protocols to access Data on
Systems in a well defined and structured manner. To use an API to access data in a system, one must have an account for this system 
through which one will be identified when a request is made. %2C is the equivalent of a comma when making an api request. 
+ is the equivalent to space."""

# Heavily rate limited proxy of https://www.geoapify.com/ api

## Define the web service address from which data would be extracted using api. Use following service for learning purpose.
#service_url = 'https://py4e-data.dr-chuck.net/opengeo?'

service_url = 'https://py4e-data.dr-chuck.net/opengeo?'


# Ignore SSL Certificate errors: Following code helps bypass the s in https.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
     # define query parameter to be parsed to the service
     address = input('Enter location')
     if len(address) < 1: break
     address = address.strip()
     parms = dict()
     parms['q'] = address
     request_url = service_url + urllib.parse.urlencode(query=parms)

     # send request to the web service
     print('Retrieving', request_url)
     uh = urllib.request.urlopen(url=request_url, context=ctx)

     # Data from web service is in utf-8. This is decoded to unicode which is a format understood by python as a string.
     data = uh.read().decode()
     #print('Retrieved',len(data), 'characters', data[:20].replace('\n', ' '))

     json_data = json.loads(data)
     print(json_data)
     for dicts in json_data['features']:
         if 'properties' in dicts.keys():
             print(dicts.keys())
             print(dicts['properties']['plus_code'])
             break
     break


  







