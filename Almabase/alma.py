session_id = "moax6gt2mfta5k768bli6tmkkwf7yu9j"
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Almabase.settings')
import requests

# url = "http://www.nitwaa.in/api/user_status"
# headers = {
# 	"Cookie":"sessionid="+session_id
# }
# r = requests.get(url, headers = headers)
# print r.content
import django
django.setup()

from Classifer.models import *

import nltk

def get_all_person(t):
        l = []
        if hasattr(t, 'node') and t.node:
            if t.node == 'PERSON':
                l.append(" ".join([child[0] for child in t]))
            else:
                for child in t:
                    l.extend(get_all_person(child))
        return l

def get_named_entities(article_text):
    sentences = nltk.sent_tokenize(article_text)
    print len(sentences)
    named_list = set()
    for sent in sentences:
        words = nltk.word_tokenize(sent)
        tagged = nltk.pos_tag(words)
        namedent = nltk.ne_chunk(tagged)
        # namedent.draw()
        named = get_all_person(namedent)
        for name in named:
            named_list.add(name)
    return list(named_list)




def search(search_parameter):
	# search_parameter = "Naveen Indala Lakshya Foundation"
	url = "http://www.nitwaa.in/api/search?q="+search_parameter

	headers = {
		"Cookie":"sessionid="+session_id
	}

	r = requests.get(url, headers = headers)
	import json
	j = json.loads(r.content)
	# print j
	results = (j["data"]["results"])

	return len(results)
	# for result in results:
	# 	print result["name"]


# articles = Article.objects.all()
# article = articles[2]

# keys=Keywords.objects.get(article=article)
# l=[k.keyword for k in keys.keywords.all()]



# from newspaper import Article
# import nltk


# url = 'http://social.yourstory.com/2013/09/how-nit-warangal-lakshya-foundation-bridged-gap-alumni-and-students/'
# article = Article(url)
# article.download()

# article.parse()

# l = get_named_entities(article.text)

# search_parameter = " ".join(l)
# for keyword in l:
# 	print keyword, search(keyword)