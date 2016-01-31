import scrapy
from scrapy.http import Request
from scrapy.spider import BaseSpider
import newspaper

with open('foo.txt') as r:
    content = r.readlines()

class DmozSpider(scrapy.Spider):
    name = "htmlget"
    start_urls=[]
    def __init__(self):
        for currentline in content:
            currentline=currentline.split('#')
            # self.allowed_domains.append(newspaper.urls.get_domain(currentline[2]))
            self.start_urls.append(currentline[2])
            # print self.allowed_domains
            print self.start_urls
    def parse(self, response):
        # print self.allowed_domains
        print self.start_urls
        filename = response.url.split("/")[-2] + '.html'
        #filename = response.url + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            f.close()
