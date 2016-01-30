# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
from scrapy.item import Item, Field
URL = "http://w3newspapers.com/"
num=1 
class getnewsitem(Item):
    url = Field()

class getnewsSpider(BaseSpider):
    name = "getnews"
    allowed_domains = ["w3newspapers.com"]
    start_urls =[
        'http://w3newspapers.com/india',
    ]
    def __init__(self):
        self.world=["afghanistan","bahrain","bangladesh","bhutan","brunei","china","cambodia","india","indonesia","iran","iraq","israel","japan","jordan","kazakhstan","kuwait","kyrgyzstan","laos","lebanon","malaysia","maldives","mongolia","nepal","oman","pakistan","palestine","philippines","qatar","singapore","syria","taiwan","tajikistan","thailand","turkey","turkmenistan","uae","uzbekistan","vietnam","yemen"]
        self.num=1 
    
    def parse(self, response):

        questions = Selector(response).xpath('//ul/li[@class="ML1"]')
        for question in questions:
            item = getnewsitem()
            item['url'] = question.xpath(
                'a[@class="thumb"]/@href').extract()[0]
            yield item
        self.num+=1    
        print URL+self.world[num]
        yield Request(URL+self.world[self.num])        
        

