from parser import *
import requests
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Almabase.settings')
import django

django.setup()
from Classifer.models import *

from multiprocessing.connection import Client
from array import array
from Queue import Queue
import threading
import time

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


workQueue = Queue()
address = ('localhost', 7001)

class myThread(threading.Thread):
    def __init__(self, threadID, name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def process_data2(self,q):
		conn = Client(address, authkey='secret password')
		message=""
		while True:
			message=conn.recv() 
			print "received", message[0],message[1]
			q.put(message)

    def run(self):
        print "Starting " + self.name
        self.process_data2(self.q)
        print "Exiting " + self.name

class myThread2(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def process_data(self,threadName, q):
        while True:
            if not q.empty():
                message = q.get()
                classifier = build_classifier()
                print "BUilt classifier"
                url = message[0]
                r = requests.get(url)
                print r.status_code
                sample_thread = Parser_Classifier(url,message[1], classifier)
                sample_thread.start()
                q.task_done()
                print "%s processing %s" % (threadName, message)
            time.sleep(1)

    def run(self):
        print "Starting " + self.name
        self.process_data(self.name, self.q)
        print "Exiting " + self.name



thread = myThread(1, "Reciever",workQueue)
thread.start()
thread = myThread2(2, "Getter", workQueue)
thread.start()