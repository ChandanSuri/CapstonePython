
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
c = raw_input("Enter Count: ")
p = raw_input("Enter position: ")
count = int(c)
pos = int(p)

while count != 0:
	f = 0
	for tag in tags:
		f = f + 1
		if f == pos:
			print tag.get('href', None)
			html = urllib.urlopen(tag.get('href', None)).read()
			soup = BeautifulSoup(html)
			tags = soup('a')
			break
	count = count - 1
	
