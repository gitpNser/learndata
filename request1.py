from urllib import request

with request.urlopen('http://news-at.zhihu.com/api/4/news/latest') as f:
	data = f.read()
	print('Status: ', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))