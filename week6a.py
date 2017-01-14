import json
import urllib

while True:
	address = raw_input("Enter the Url: ")
	if len(address) < 1: break
	data = urllib.urlopen(address).read()
	f_data = json.loads(data)
	ls = f_data["comments"]
	print len(ls)
	s = 0
	for c in ls:
		s = s + int(c["count"])
	print "Sum is => ",s
