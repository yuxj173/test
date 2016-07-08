import sys
import time
import urllib.request
from bs4 import BeautifulSoup

domain = 'http://www.istartedsomething.com/bingimages/'

def single(url):
    page = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    for a in page.findAll('a', class_ = 'cn'):
        print(1)
        name = a.find('img', class_ = 'lazy')['data-original'][13:-6]
        img = domain + 'cache/' + name
        file = open(name, 'wb')
        file.write(urllib.request.urlopen(img).read())
        file.close()

single(domain)
