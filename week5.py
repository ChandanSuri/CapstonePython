import urllib
import xml.etree.ElementTree as ET

while True:
	s = 0
	address = raw_input('Enter Lovation: ')
	if len(address) < 1: break
	print 'Retrieving', address
	data = urllib.urlopen(address).read()
	print 'Retrieved', len(data), 'characters'
	tree = ET.fromstring(data)
	counts = tree.findall('.//count')
	print len(counts)
	for c in counts:
		s = s + int(c.text)
	print s
		
	
	
	

