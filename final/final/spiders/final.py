import scrapy
from scrapy.http import Request
from scrapy.spiders import BaseSpider
import newspaper

with open('foo.txt') as r:
    lines = r.readlines()

from multiprocessing.connection import Listener
from array import array
import requests



class DmozSpider(scrapy.Spider):
    name = "htmlget"
    start_urls=[]
    def __init__(self):
        super(DmozSpider, self).__init__()
        address = ('localhost', 7003)     # family is deduced to be 'AF_INET'
        listener = Listener(address, authkey='secret password')
        self.conn = listener.accept()
        print "STarting server XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        print 'connection accepted from', listener.last_accepted
        for currentline in lines:
            # currentline=currentline.split(',')
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