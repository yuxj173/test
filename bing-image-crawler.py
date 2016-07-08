# 
# python3 coding

import urllib.request
from bs4 import BeautifulSoup

domain = 'http://www.istartedsomething.com/bingimages/'

def single(url):
    page = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    for a in page.findAll('a', class_ = 'cn'):
        date = a['href'][1:-3]
        name = a.find('img', class_ = 'lazy')['data-original'][13:-6]
        print('catching %s - %s...'%(date, name), end = '', flush = True)
        
        img = domain + 'cache/' + name
        file = open(date + '-' + name, 'wb')
        file.write(urllib.request.urlopen(img).read())
        file.close()
        
        print('done.')

single(domain)
