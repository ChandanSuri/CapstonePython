import json
import urllib

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
while True:
	address = raw_input("Enter the Location: ")
	if len(address) < 1: break
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
	print "Retrieving ", url
	data = urllib.urlopen(url).read()
	try : js = json.loads(str(data))
	except: 
		js = None
	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure To Retrieve ===='
		print data
		continue
	print json.dumps(js, indent=4)
	place_id = js['results'][0]['place_id']
	print "Place Id is: ", place_id
	
