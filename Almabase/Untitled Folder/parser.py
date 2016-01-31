import threading
import time
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Almabase.settings')

import django
import newspaper
import unicodedata
import nltk
from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier


django.setup()




class Parser_Classifier(threading.Thread):
    def __init__(self, response_body, classifier):
        threading.Thread.__init__(self)
        self.response_body = response_body
        self.classifier = classifier

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

    def add_article(title,summary,url,author,keywords1):
        a=Article.objects.get_or_create(title=title,summary=summary,url=url,author=author)[0]
        a.save()
        article=a
        articleid=a.id
        a=Keywords.objects.get_or_create(article=a)[0]
        print a
        print a.keywords
        for key in keywords1:
            k=KeywordList.objects.get_or_create(keyword=key)[0]
            k.save()
            if not k.keywords_set.filter(id=a.id):
                a.keywords.add(k)
                a.save()
        return article


    def classify(article,newClassifier):
        keys=Keywords.objects.get(article=article)
        print keys
        l=[k.keyword for k in keys.keywords.all()]
        test_string=" ".join(l)
        print test_string
        classification = newsClassifier.classify(test_string)
        print classification
        print type(classification)

    def parse_add(response_body):
        a=newspaper.Article("")
        a.is_downloaded = True
        a.parse()
        a.nlp()

        l1= get_named_entities(a.text)
        author="default"
        try:
            author=a.author[0]
        except:
            print "Not found"
        art=add_article(a.title,a.summary,url,author,l1)
        # test_keywords(art,newsClassifier)
        return art





    def run(self):
        print "Starting thread...", 
        # labeled_articles = [(a, a.relevant) for a in Article.objects.all()[:(len(Article.objects.all()))]]
        # print labeled_articles
        # featuresets=[]
        # for (article, relevant) in labeled_articles:
        #   r=article_keywords(article)
        #   featuresets.append((r,relevant))
        # print featuresets
        # train_set, test_set = featuresets[:(len(featuresets))], featuresets[(len(featuresets)-2):]
        # print train_set
        # newsTrainer = Trainer(tokenizer)
        # for f in train_set:
        #     newsTrainer.train(f[0]['keyword'],f[1])
        # newsClassifier = Classifier(newsTrainer.data, tokenizer)
        # url=raw_input("Enter the url: ")

        added_article = parse_add(self.response_body)
        classify(added_article, self.classifier)
