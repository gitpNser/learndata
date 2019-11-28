# -*- coding: utf-8 -*-
import scrapy
import re

class StocksSpider(scrapy.Spider):
    name = 'stocks'
    #allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stock_list.html']

    def parse(self, response):

        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][hz]\d{6}',href[0])
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue
    
    def parse_stock(self,response):
        
        infoDict = {}
        
        stockInfo = response.css('.stock_bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        
        # to be continued
        # after complete this file, need to update file of item pipeline
        # if changed the object name of item pipeline, need to change the setting file as well
        