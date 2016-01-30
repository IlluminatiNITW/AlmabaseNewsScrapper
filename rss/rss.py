import feedparser
d = feedparser.parse('http://www.reddit.com/r/python/.rss')

#Print the title of the feed
print d['feed']['title']

#resolves relative links
print d['feed']['links']

#print escaped HTML
print d.feed.subtitle

#print no. of entries
print len(d['entries'])

#each entry in feed is a dictionary. printing 1st entry
print d['entries'][0]p['title']

#printing first entry and its link
print d['entries'][0]['link']

#loop to print all posts and their links
for post in d.entries:
	print post.title + ":" + post.link + "\n"

#Reports the feed type and version
print d.version  

#Full access to all HTTP headers
print d.headers     

#Just get the content-type from the header\
print d.headers.get('content-type')

