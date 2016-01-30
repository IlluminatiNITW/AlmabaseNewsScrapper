from newspaper import Article
import unicodedata


def getkeywords(filename):
	with open(filename) as f:
		a = [x.strip('\n') for x in f.readlines()]
		return a
	return []


def getsimilar(l1,l2):
	return len(set(l1)&set(l2))

def difference(l1,l2):
	return list(set(l1) - set(l2))


def train(urls,keywords):
	for url in urls:
		a=Article(url)
		a.download()
		a.parse()
		a.nlp()
		print a.title
		print a.summary
		print a.keywords
		l1=a.keywords
		l1_1=[]
		for word in l1:
			l1_1.append(unicodedata.normalize('NFKD', word).encode('ascii','ignore'))
		diff=difference(l1_1,keywords)
		keywords.extend(diff)
	return keywords


def getrelevance(url,keywords):
	a=Article(url)
	a.download()
	a.parse()
	a.nlp()
	print a.title
	print a.summary
	l1=a.keywords
	no=getsimilar(l1,keywords)
	print keywords
	print l1
	print "Similar words: "
	print no
	print len(keywords)
	print "Match: "
	print float(no)/(len(keywords))

keywords=getkeywords('keywords.txt')
print "Keywords"
print keywords
url_list=['http://social.yourstory.com/2013/09/how-nit-warangal-lakshya-foundation-bridged-gap-alumni-and-students/','http://www.thehindu.com/news/national/telangana/nit-warangal-mired-in-controversy/article8024968.ece','http://www.pagalguy.com/articles/nit-warangal-city-carved-out-of-a-single-stone-32595429']
keywords=train(url_list,keywords)
print "Training complete"
print keywords
url='http://www.pagalguy.com/articles/students-get-sabji-without-vegetables-and-raw-chappatis-at-n-38664708'
getrelevance(url,keywords)



