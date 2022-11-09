import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
#Enter location:  http://py4e-data.dr-chuck.net/comments_97410.xml
#Retrieving  http://py4e-data.dr-chuck.net/comments_97410.xml
#Retrieved 4220 characters
#Count: 50
#Sum: 2259

import urllib.request as ur
import xml.etree.ElementTree as et
#needed to have xml work

url = input('Enter location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml'

total_number = 0
sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
#turns xml into a readable string
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
#finds the //counts of the entire section
for count in counts:
    sum += int(count.text)
    #adds together all of the numbers that are in the //counts
    total_number += 1
    #counts the number of //counts in the tree

print('Count:', total_number)
print('Sum:', sum)
#printing of the desired output

#other solution that does not compeltely work
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#import ssl
#import re
#summ = 0
#numm = 0
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#html = urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, "html.parser")
#tags = soup('count')
#prints all count
#for tag in tags:
    #texts = tag
    #for num in texts:
        #numm = re.findall('([0-9]+)', num)
        #for nums2 in numm:
            #finalnum = int(nums2)
            #summ = summ + finalnum
#print(summ)
