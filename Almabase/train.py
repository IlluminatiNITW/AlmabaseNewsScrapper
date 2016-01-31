import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Almabase.settings')

import django
import newspaper
import unicodedata
import nltk

django.setup()

def get_all_person(t):
    l = []
    if hasattr(t, 'node') and t.node:
        if t.node == 'PERSON':
            l.append(" ".join([child[0] for child in t]))
        else:
            for child in t:
                l.extend(get_all_person(child))
    return l

def get_all_organizations(t):
    l = []
    if hasattr(t, 'node') and t.node:
        if t.node == 'ORGANIZATION':
            l.append(" ".join([child[0] for child in t]))
        else:
            for child in t:
                l.extend(get_all_organizations(child))
    return l


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
    person_list = set()
    org_list = set()
    for sent in sentences:
        words = nltk.word_tokenize(sent)
        tagged = nltk.pos_tag(words)
        namedent = nltk.ne_chunk(tagged, binary = True)
        namedent2 = nltk.ne_chunk(tagged)
        named = get_all_named(namedent)
        for name in named:
            named_list.add(name)
        persons = get_all_person(namedent2)
        orgs = get_all_organizations(namedent2)
        for person in persons:
            person_list.add(person)
        for org in orgs:
            org_list.add(org)
        return list(named_list), list(person_list), list(org_list)

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


def add_article(title,summary,url,author, img_link ,keywords1, persons, orgs):
    a=Article.objects.get_or_create(title=title,summary=summary,url=url,author=author, image_link = img_link)[0]
    a.save()
    article=a
    articleid=a.id
    a=Keywords.objects.get_or_create(article=a)[0]
    b=PersonList.objects.get_or_create(article = article)[0]
    c=OrganizationList.objects.get_or_create(article=article)[0]
    print a
    print a.keywords
    for key in keywords1:
        k=KeywordList.objects.get_or_create(keyword=key)[0]
        k.save()
        if not k.keywords_set.filter(id=a.id):
            a.keywords.add(k)
            a.save()
    for person in persons:
        k=Person.objects.get_or_create(name=person)[0]
        k.save()
        if not k.personlist_set.filter(id=b.id):
            b.persons.add(k)
            b.save()
    for org in orgs:
        k=Organization.objects.get_or_create(name=org)[0]
        k.save()
        if not k.organizationlist_set.filter(id=c.id):
            c.orgs.add(k)
            c.save()

    return article

def train(urls,keywords):
	for url in urls:
		a=newspaper.Article(url)
		a.download()
		a.parse()
		a.nlp()
        img_link = a.imgs[0]
        named, persons, orgs= get_named_entities(a.text)
        author="default"
        try:
            author=a.author[0]
        except:
            print "Not found"
        art=add_article(a.title,a.summary,url,author,img_link, named, persons, orgs)
        # test_keywords(art,newsClassifier)
	return keywords

def populate():
	print "Training the classifier....adding keywords"
	url_list=['http://www.pagalguy.com/articles/nit-warangal-city-carved-out-of-a-single-stone-32595429','http://social.yourstory.com/2013/09/how-nit-warangal-lakshya-foundation-bridged-gap-alumni-and-students/','http://www.thehindu.com/news/national/telangana/nit-warangal-mired-in-controversy/article8024968.ece']
	keywords=KeywordList.objects.all().values_list('keyword',flat=True)
	print keywords
	keywords=train(url_list,keywords)

	

if __name__ == '__main__':
    print "Starting Stark population script..."
    populate()