import scrapy
from scrapy.http import Request
from scrapy.spider import BaseSpider

r = open('test.txt', 'r')
text=r.read()
lines = text.split("\n")
print lines
class DmozSpider(scrapy.Spider):
    name = "htmlget"
    allowed_domains=[]
    start_urls=[]
    def __init__(self):
        for currentline in lines:
            currentline=currentline.split(',')
            self.allowed_domains.append(currentline[0])
            self.start_urls.append(currentline[1])
    def parse(self, response):
        print self.allowed_domains
        print self.start_urls
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        currentline=r.readline().split(",")