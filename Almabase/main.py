from parser import *
import requests
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Almabase.settings')
import django

django.setup()
from Classifer.models import *


def article_keywords(article):
    keys=Keywords.objects.get(article=article)
    # print keys
    l=[k.keyword for k in keys.keywords.all()]
    # print " ".join(l)
    keyset={'keyword':" ".join(l)}
    return keyset


def build_classifier():
    print "Starting testing of Bayes Classifer"
    labeled_articles = [(a, a.relevant) for a in Article.objects.all()]
    print "labeled articles ", labeled_articles
    featuresets=[]
    for (article, relevant) in labeled_articles:
    	r=article_keywords(article)
    	featuresets.append((r,relevant))

    # print featuresets
    train_set = featuresets
    # print train_set
    newsTrainer = Trainer(tokenizer)
    for f in train_set:
        newsTrainer.train(f[0]['keyword'],f[1])
    newsClassifier = Classifier(newsTrainer.data, tokenizer)
    return newsClassifier



if __name__ == '__main__':
    classifier = build_classifier()
    print "BUilt classifier"
    r = requests.get("http://social.yourstory.com/2013/09/how-nit-warangal-lakshya-foundation-bridged-gap-alumni-and-students/")
    print r.status_code
	# sample_thread = Parser_Classifier(r.content, classifier)
	# sample_thread.start()
