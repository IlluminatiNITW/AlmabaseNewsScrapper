import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Almabase.settings')

import django
import newspaper
import unicodedata
import nltk

django.setup()

from Classifer.models import *



def article_keywords(article):
	keys=Keywords.objects.get(article=article)
	print keys
	l=[k.keyword for k in keys.keywords.all()]
	keyset=[]
	for k in l:
		keyset.append({'keyword':k})
	return keyset


if __name__ == '__main__':
    print "Starting Stark population script..."
    labeled_articles = [(a, a.relevant) for a in Article.objects.all()]
    print labeled_articles
    featuresets=[]
    for (article, relevant) in labeled_articles:
    	r=article_keywords(article)
    	for keys in r:
    		featuresets.append((keys,relevant))
    print featuresets
    train_set, test_set = featuresets[:(len(featuresets))], featuresets[(len(featuresets)-2):]
    print train_set
    classifier = nltk.NaiveBayesClassifier.train(train_set)
