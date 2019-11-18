from html.parser import HTMLParser
from urllib import request
import re

class MyHTMLParser(HTMLParser):
	def __init__(self):
		super(MyHTMLParser, self).__init__()
		self.__parsedata = ''	# set a null position
	
	def handle_starttag(self, tag, attrs):
		
		if('class', 'event-title') in attrs:
			self.__parsedata = 'name' # find out whether this tag is what we look for through attrs
		if tag == 'time':
			self.__parsedata = 'time'
		if('class', 'say-no-more') in attrs:
			self.__parsedata = 'year'
		if('class', 'event-location') in attrs:
			self.__parsedata = 'location'
		
	def handle_endtag(self, tag):
		self.__parsedata = ''	#Clear the position when end of html tag
	
	def handle_data(self, data):
		if self.__parsedata == 'name':
			print('会议名称： %s' % data)
		if self.__parsedata == 'time':
			print('会议时间： %s' % data)
		if self.__parsedata == 'year':
			if re.match(r'\s\d{4}', data):
				print('会议年份： %s' % data.strip())
		if self.__parsedata == 'location':
			print('会议地点 ： %s' % data)
			print('-----------------------------------')
			
parser = MyHTMLParser()

URL = 'https://www.python.org/events/python-events/'

with request.urlopen(URL, timeout=15) as f:
	data = f.read()
parser.feed(data.decode('utf-8'))
	