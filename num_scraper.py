## urllib turns a URL into a file
import urllib
from BeautifulSoup import *

url = input("Enter URL - ")
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')

for tag in tags:
	print(tag.get('href', None))
        
