# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BiqugePipeline(object):
    def open_spider(self, spider):
        
        self.f = open('biquge33322.txt','w')
        
    def close_spider(self, spider):
        
        self.f.close()
    
    def process_item(self, item, spider):
        
        try:
#            line1 = str(dict(item)['章名'])[5:-2] + '\n'
#            self.f.write(line1)
#            line2 = str(dict(item['内容'])) + '\n'
#            self.f.write(line2)
            line = str(dict(item)) + '\n'
            self.f.write(line)
            
        except:
            pass
        
        return item
