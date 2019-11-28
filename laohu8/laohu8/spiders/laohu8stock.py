# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup

class Laohu8stockSpider(scrapy.Spider):
    name = 'laohu8stock'
#    allowed_domains = ['https://www.laohu8.com/stock/']
    start_urls = ['http://quote.eastmoney.com/stock_list.html']
    
    def parse(self, response):
        
        for href in response.css('a::attr(href)').extract():
            
            try:
                stock =re.findall(r'[s][hz]\d{6}',href)[0]
                url = 'https://www.laohu8.com/stock/' + stock[2:]
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue
    
    def parse_stock(self, response):
        
        infoDict = {}
        
        data = response.body
        
#        soup = BeautifulSoup(response,'lxml')
        soup = BeautifulSoup(data, 'lxml')
        
        stockinfo = soup.find('div',attrs={'class':'detail-data'})
        
        keylist = stockinfo.find_all('dt')
        valuelist = stockinfo.find_all('dd')
        
        key = []
        val = []
            
        for td in keylist:
            key.append(td.string)
            
        for dd in valuelist:
            val.append(dd.string)
        
        for i in range(len(key)):
            infoDict[key[i]] = val[i]
        
        yield infoDict
