# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
count2 = 0
count1 = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#enter the Url to start
#how long do you repeat
#position of url
url = input('Enter - ')
count11 = int(input('Enter count: '))
position = int(input ('Enter position: '))

# range between 0 and the imputed count
for count1 in range(0, count11):
    html = urllib.request.urlopen(url, context=ctx).read()
    #cleans up the html code
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #finds position imputed at start(list starts at 0 thats why subtracting)
    url = tags[position-1].get('href', None)
    count1 = count1 + 1

print(url)
