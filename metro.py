############################################
# Tokyo Metro API
# ---------------------------------
# Created by  : Adam Nguyen
# Updated by  : Adam Nguyen
# Created at  : 09/23/2014
# Updated at  : xx/xx/xxxx
# Description : API via Python
#############################################
#On APIs: https://www.youtube.com/watch?v=FknvOGcLHmc

#Names of working directory and files
myfolder = "C:/Users/adam.nguyen/Desktop/Python/"

#Load libraries
from urllib2 import Request, urlopen, URLError, urlopen
import urllib2, string, requests, os, sys, re, json, webbrowser

#Set Directory
os.chdir(myfolder)
os.getcwd()

#Create a text file with inputs
def textfile(text, name):
    try:
        text_file = open(name, 'w')
        text_file.write(text)
        text_file.close()
        return(text_file)
    except:
        print('Input Error')

#Pattern matching function
def Find(pat, text):
    match = re.search(pat, text)
    if match:
        print match.group() #0, blank string, none
        return(match.group())
    else:
        print 'Pattern Not Found'

#Create a local search function
def local_search(field, field2 = None):
    api_key = '2dc043c67d9835afd6380b77019504c369cf612593deaae6acceba3206403c86'
    url = 'https://api.tokyometroapp.jp/api/v2/datapoints?acl:consumerKey=' + api_key
    final_url = url + '&rdf:type=odpt:' + field
    if field2 == None:
        print final_url
        return final_url
    else:
        final_url2 = final_url + '&odpt:station=odpt.Station:' + field2
        print final_url2
    return final_url2


#Stream Timetable Data from Metro API
api_data = requests.get(local_search('StationTimetable', 'TokyoMetro.Hanzomon.OmoteSando'))
#api_data = requests.get(local_search('StationTimetable'))
api_data.json()[0]

#Open link in Chrome
webbrowser.open(local_search('StationTimetable', 'TokyoMetro.Hanzomon.OmoteSando'), 2)

webbrowser.open(local_search('Information'), 2)


#Create JSON object
api_data.json()[0]

#Get keys for one dictionary item
key_list = api_data.json()[1].keys()
print key_list

#Create data column
x = 0
for item in api_data.json():
    print item['odpt:weekdays']

for jsonData in api_data.json()[0]:
    for item in jsonData:
        print item.get("odpt:departureTime")


data = api_data.json()[1]
data2 = data.get("odpt:departureTime")

#Stream second table
api_data2 = requests.get(local_search('Station'))
api_data2.json()

forecaster_file = open('C:/Users/adam.nguyen/Desktop/forecaster.json')
forecaster_json = json.load(forecaster_file)


import matplotlib.pyplot as plt
plt.plot(
forecaster_json.values



###Appendix
#Sample API pathway
odpt:station=odpt%3Astation

#Check header
print api_data.headers

#Create JSON object
res_json = api_data.json()

#Get keys for one dictionary item
key_list = res_json[1].keys()

#Create data column
x = 0
for item in res_json:
    print item['odpt:trainNumber']
    x += 1
    print x

#Create a text file
textfile(api_data.text, "newfile.txt")

#Search within text file for first pattern
res_search = Find('{(.*?)}', str(api_data.text))

#Put all instances into a list
res_findall = re.findall('{(.*?)}', str(api_data.text), re.DOTALL)

#Final last instance
res_findall[len(res_findall) - 1]

#Create list for all loops
for section in range(len(res_findall)):
    print res_findall[section]




