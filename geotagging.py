import urllib
import json

surl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    add = raw_input("Enter address:")
    if len(add) < 1 : break

    url = surl + urllib.urlencode({"sensor" : "false", "address" : add})
    print "Retreiving", url
    fh = urllib.urlopen(url)
    data = fh.read()
    print "Retreived", len(data), "characters"

    try: js = json.loads(str(data))
    except: js = None

    if 'status' not in js or js['status'] != 'OK':
        print "---Failed---"
        print data
        continue

    print json.dumps(js, indent = 4)
    
    lat = js['results'][0]['geometry']['location']['lat']
    lon = js['results'][0]['geometry']['location']['lng']

    print "Latitude:", lat
    print "Longitude:", lon
