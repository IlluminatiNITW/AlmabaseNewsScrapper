import requests  
import feedparser
from bs4 import BeautifulSoup  
from time import sleep

website_list =["http://rss.cnn.com/rss/edition.rss",
"http://yourstory.com/feed/",
"http://economictimes.indiatimes.com/rssfeedsdefault.cms"]

fo = open("foo.txt", "wb")
#website_url = "http://yourstory.com/feed/"
for website_url in website_list:

    d = feedparser.parse(website_url)

    for post in d.entries:
        print "Time Stamp : "
        print post.published
        print "News Website url : "
        print post.summary_detail.base
        print "Article URL : "
        print post.id
        fo.write(post.id)
        fo.write("\n")
        print "Article Title : "
        print post.title
        print "Article Content : "
        print post.summary_detail.value
        print "____________________________________________________"
      
fo.close()







