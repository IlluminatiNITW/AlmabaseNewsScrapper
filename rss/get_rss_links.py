import requests  
import feedparser
from bs4 import BeautifulSoup  
from time import sleep
from config import configs

website_list =["http://rss.cnn.com/rss/edition.rss",
"http://yourstory.com/feed/",
"http://economictimes.indiatimes.com/rssfeedsdefault.cms",
"https://news.ycombinator.com/rss"]

fo = open("foo.txt", "wb")
#website_url = "http://yourstory.com/feed/"
for website_url in website_list:

    d = feedparser.parse(website_url)

    for post in d.entries:
        fo.write(website_url+'#')
        print "Time Stamp : "
        print post.published
        fo.write(post.published+'#')
        print "News Website url : "
        print post.summary_detail.base
        print "Article URL : "
        link = post[configs[website_url]["link"]]
        print link
        fo.write(link)
        fo.write("\n")
        print "Article Title : "
        print post.title
        print "Article Content : "
        print post.summary_detail.value
        print "____________________________________________________"
      
fo.close()







