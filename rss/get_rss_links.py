'''
=============================================================================
Feed fetcher
=============================================================================
Input files: 
    sites.txt: stores the article feed sites.
    date.txt: Stores the last fetched date.

Output files:
    ../final/foo.txt: stores the article links

This script gets the article links based on last fetched time. 
Config.py stores the configs for specific rss site.
'''

import requests  
import feedparser
from bs4 import BeautifulSoup  
from time import sleep
from config import configs
import datetime
from email.utils import parsedate_tz


with open('sites.txt') as r:
    content = r.readlines()
with open('date.txt') as r:
    date = r.readlines()
#Reading last fetched date
if len(date) == 0:
    date=""
else:
    date=parsedate_tz(date[0])
    date=datetime.datetime(*date[0:6])
    print type(date)
#Get the rss links
for item in content:
    item = item.split(',')
website_list = item
for website_list in content:
    website_list=website_list.split(',')
print website_list
flag=0
print "Last fetched date: ",date
#Writing to output file
fo = open("../final/foo.txt", "wb")
for website_url in website_list:
    d = feedparser.parse(website_url)
    for post in d.entries:
        #Writing the most recent last fetched date to file
        if flag == 0:
            fdate = open("date.txt", "wb")
            fdate.write(post.published)
            fdate.close()
            flag=1
        post_date=datetime.datetime(*(parsedate_tz(post.published))[0:6])
        if date != "" and  post_date <= date:
            break
        print "Time Stamp : "
        print post.published
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







