import urllib
import sys
import struct
import urllib.request
import json
from bs4 import BeautifulSoup


#stdin and decoding
def getMessage():
      raw = sys.stdin.read(4)
      if not raw:
          sys.exit(0) #error
       unpacked = struct.unpack('=I', raw)[0]
       url_ = sys.stdin.read(unpacked)
       return json.loads(url_)
url = 'https://twitter.com/realDonaldTrump'  # type: str
usable = urllib.request.urlopen(url)
soup = BeautifulSoup(usable, "lxml")  # what parser do we use

while True:
    getMessage()

print (soup.title.text)