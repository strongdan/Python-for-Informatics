##Scraping Numbers from HTML using BeautifulSoup
##In this assignment you will write a Python program similar to urllink2.py
##The program will use urllib to read the HTML from the data files below
##and parse the data, extracting numbers and compute the sum of the numbers
##in the file.

import urllib
from BeautifulSoup import *

url = input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

##find lines that begin with <tr>


##find all the <span> tags in the file and pull out the numbers from the tag
##and sum the numbers

tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print ( 'TAG:',tag )
    print ( 'URL:',tag.get('href', None) )
    print ( 'Contents:',tag.contents[0] )
    print ( 'Attrs:',tag.attrs )
