import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Almabase.settings')

import django
import newspaper
import unicodedata
import nltk

django.setup()


def get_all_named(t):
    l = []
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            l.append(" ".join([child[0] for child in t]))
        else:
            for child in t:
                l.extend(get_all_named(child))
    return l

def get_named_entities(article_text):
    sentences = nltk.sent_tokenize(article_text)
    print len(sentences)
    named_list = set()
    for sent in sentences:
        words = nltk.word_tokenize(sent)
        tagged = nltk.pos_tag(words)
        namedent = nltk.ne_chunk(tagged, binary = True)
        named = get_all_named(namedent)
        for name in named:
            named_list.add(name)
    return list(named_list)


def getkeywords(filename):
	with open(filename) as f:
		a = [x.strip('\n') for x in f.readlines()]
		return a
	return []


def getsimilar(l1,l2):
	return len(set(l1)&set(l2))

def difference(l1,l2):
	return list(set(l1) - set(l2))


from Classifer.models import *


def add_article(title,summary,url,author,keywords1):
	a=Article.objects.get_or_create(title=title,summary=summary,url=url,author=author,relevant=False)[0]
	a.save()
	a=Keywords.objects.get_or_create(article=a)[0]
	print a
	print a.keywords
	for key in keywords1:
		k=KeywordList.objects.get_or_create(keyword=key)[0]
		k.save()
		if not k.keywords_set.filter(id=a.id):
			a.keywords.add(k)
			a.save()

def train(urls,keywords):
	for url in urls:
		a=newspaper.Article(url)
		a.download()
		a.parse()
		a.nlp()
		l1=get_named_entities(a.text)
		add_article(a.title,a.summary,url,a.authors[0],l1)
	return keywords

def populate():
	print "Training the classifier....adding keywords"
	url_list=['http://yourstory.com/2016/01/invest-karnataka-begaum-hubli-dharwad/','http://yourstory.com/2015/07/ameera-shah/','http://yourstory.com/2015/08/college-startups/']
	keywords=KeywordList.objects.all().values_list('keyword',flat=True)
	print keywords
	keywords=train(url_list,keywords)

	

if __name__ == '__main__':
    print "Starting Stark population script..."
    populate()