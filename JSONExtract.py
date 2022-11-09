import urllib.request, urllib.parse, urllib.error
import json
url = "http://py4e-data.dr-chuck.net/comments_1314569.json"
print("Retrieving: ", url)
total = 0
i = -1

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), 'characters')
js = json.loads(data)

while True:
    i = i + 1
    try:
        total = total + int(js["comments"][i]["count"])
    except:
        break
print("Sum:", total)


#import json
#import urllib
#count = 0

#url = "http://python-data.dr-chuck.net/comments_283400.json"
#print "retrieving URL. Stand by."
#uh = urllib.urlopen(url)
#data= uh.read()

#info = json.loads(data)
#for item in info["comments"]:
	#print item["count"]
	#number = int(item["count"])
	#count = count + number
#print count
