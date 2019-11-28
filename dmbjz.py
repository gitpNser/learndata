from html.parser import HTMLParser
from urllib import request
import re

class MyHTMLParser(HTMLParser):
	def __init__(self):
		super(MyHTMLParser, self).__init__()
		self.__parserdata = ''
		
	def handle_starttag(self, tag, attrs):
		# if tag == 'title':
		#	 self.__parserdata = 'title'
		if tag == 'dd':
			self.__parserdata = 'dd'
		if tag == 'dd':
			if tag == 'a':
				for name, value in attrs:
					if name =='href':
						self.__parserdata = 'href'
				
	
	def handle_endtag(self, tag):
		self.__parserdata = ''
		
	def handle_data(self, data):
		if self.__parserdata == 'dd':
			print('章节名称： %s' % data)
		if self.__parserdata == 'href':
			print('链接: -> %s' % data)
			print('---------------------')

parser = MyHTMLParser()

URL = 'https://www.biquge.info/48_48350/'

with request.urlopen(URL, timeout=15) as f:
	data = f.read()
parser.feed(data.decode('utf-8'))