from html.parser import HTMLParser
from urllib import request
import re

class MyParser(HTMLParser):
    
	def __init__(self):
       
	   HTMLParser.__init__(self)
       
	def handle_starttag(self, tag, attrs):
		
		if tag == 'dd':
			print(str(content.decode('utf-8')))
	
		if tag == 'a':
			for name,value in attrs:
				if name == 'href' and value.startswith('4'):
					print(value)
					print('------------------')

if __name__ == '__main__':
    url='https://www.biquge.info/48_48350/'
    content = request.urlopen(url).read()
    my = MyParser()
    my.feed(content.decode('utf-8'))
    my.close()