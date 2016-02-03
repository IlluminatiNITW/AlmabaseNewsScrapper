import requests  
import feedparser
from bs4 import BeautifulSoup  
from time import sleep
from config import configs


with open('sites.txt') as r:
    content = r.readlines()
print len(content)
for item in content:
    item = item.split(',')
website_list = item
for website_list in content:
    website_list=website_list.split(',')
print website_list
website_list.pop()

fo = open("../final/foo.txt", "wb")
website_url = "https://nitwarangal101.wordpress.com/comments/feed/"
# for website_url in website_list:

d = feedparser.parse(website_url)
print d

for post in d.entries:
    # fo.write(website_url+',')
    print post
    print "Time Stamp : "
    print post.published
    print post.feed.updated
    #fo.write(post.published+'#')
    print "News Website url : "
    # print post.summary_detail.base
    # print "Article URL : "
    # link = post[configs[website_url]["link"]]
    # print link
    # fo.write(link)
    # fo.write("\n")
    # print "Article Title : "
    # print post.title
    # print "Article Content : "
    # print post.summary_detail.value
    print "____________________________________________________"
      
fo.close()







