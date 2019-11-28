# -*- coding: utf-8 -*-
import scrapy
import re
#from bs4 import BeautifulSoup


class BiqugebookSpider(scrapy.Spider):
    name = 'biqugebook'
#    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/3/3322']

    def parse(self, response):
 
        for href in response.css('a::attr(href)').extract():
            pattern = re.compile(r"/3/3322/\d+")
            try:
                chapter = re.findall(pattern, href)[0]
                url = 'http://www.xbiquge.la/' + chapter + '.html' 
                yield scrapy.Request(url, callback=self.parse_chapter)
            except:
                continue
        
#        pattern = re.compile("<dd><a href=(.*?)>(.*?)</a></dd>")
#        
#        try:
#            chapter = re.findall(pattern, response.extract())[0]
#            url = 'http://www.xbiquge.la/' + chapter
#            yield scrapy.Request(url, callback=self.parse_chapter)
#        except:
#            pass
        
        
        
    def parse_chapter(self, response):
        
#        soup = BeautifulSoup(response, 'lxml')
#        
#        content = soup.find("div",{"id":"content"}).get_text()
#        
#        title = soup.find('title').string
 
        title = response.css('h1').extract()
        title = re.findall(r'>(.*?)</h1>',title[0])
#        title = title[5:]
#        content = response.css('div','id:content::text')
        contents = response.xpath('//*[@id="content"]/text()')
        content = ''
        
        for each in contents:
            if len(each.re('\S+')) > 0:
                content += each.re('\S+')[0]
        
#        content = re.findall(r'>(.*?)</div>', content)
        
#        book_content = []
#        book_content.append(title)
#        book_content.append('\n')
#        book_content.append(content)

        
        infoDict = {}
        
        infoDict['章名'] = title
        infoDict['内容'] = content
        
        yield infoDict
#        yield book_content