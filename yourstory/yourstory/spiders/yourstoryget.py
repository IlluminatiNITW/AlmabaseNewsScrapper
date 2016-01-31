# -*- coding: utf-8 -*-
import scrapy

from scrapy import Spider
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
from yourstory.items import StackItem




# URL = "http://www.yourstory.com/2014/3/%d"
URL = "http://www.yourstory.com/2016/%d"

class YourstorygetSpider(BaseSpider):
    name = "yourstoryget"
    allowed_domains = ["yourstory.com"]
    start_urls =[
        'http://www.yourstory.com/2016',
    ]

    def __init__(self):
        self.page_number = 26
    
    def parse(self, response):
        print self.page_number
        print "----------"

        questions = Selector(response).xpath('//li[@class="grid-full mb-30"]')
        if not questions:
            raise CloseSpider('No more pages')
        
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="block"]/div[@class="fl content"]/div[@class="title-small bentonCondensed bold color-black-2 truncate-2"]/text()').extract()[0]
            item['text'] = question.xpath(
                'a[@class="block"]/div[@class="fl content"]/p/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="block"]/@href').extract()[0]
            #if "NIT" in item['text']: 
            yield item
               


        self.page_number +=1
        print self.page_number
        yield Request(URL % self.page_number)


