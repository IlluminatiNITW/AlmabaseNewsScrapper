import scrapy
from scrapy.http import Request
from scrapy.spider import BaseSpider
import newspaper



from multiprocessing.connection import Listener
from array import array
import requests



class DmozSpider(scrapy.Spider):
    name = "htmlget"
    start_urls=[]
    def __init__(self):
        super(DmozSpider, self).__init__()
        with open('test.txt') as r:
            content = r.readlines()
        address = ('localhost', 7003)     # family is deduced to be 'AF_INET'
        listener = Listener(address, authkey='secret password')
        self.conn = listener.accept()
        print "STarting server XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        print 'connection accepted from', listener.last_accepted
        for currentline in content:
            # self.allowed_domains.append(currentline[0])
            self.start_urls.append(currentline)
    def parse(self, response):
        # print self.allowed_domains
        print self.start_urls

        r = response
        # filename = response.url.split("/")[-2] + '.html'
        self.conn.send([r.url,r.body])
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # currentline=r.readline().split(",")