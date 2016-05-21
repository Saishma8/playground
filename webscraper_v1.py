#code to open a page and go to a link at specific position and follow the link and repeat the process a set number of times

import re
import urllib
from bs4 import BeautifulSoup

page = raw_input("Enter page:")
count = int(raw_input("Enter count:"))
position = int(raw_input("Enter position:"))
start = int(0)
url2 = page

def url(page,position):
    html = urllib.urlopen(page).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    url2 = tags[position-1].get('href',None)
    return url2

while start < count:
     url2 = url(url2,position);
     start = start + 1

print re.findall('known_by_(.*).html',url2)[0]

