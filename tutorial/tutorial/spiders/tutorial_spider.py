import scrapy
from scrapy.spiders import SitemapSpider
from tutorial.items import HyderabadItem

class TutorialSpider(scrapy.Spider):
    name = "tutorial"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc



class YourStorySpider(SitemapSpider):
    name = 'yourstory'
    count = 0
    sitemap_urls = ['http://yourstory.com/sitemap_index.xml']

    def parse(self, response):
        # print "HIT: ", response.url
        # print "---------------------------", response.body
        self.count = self.count + 1
        if "hyderabad" in response.body.lower():
            print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            item = HyderabadItem()
            item['link'] = response.url
            yield item