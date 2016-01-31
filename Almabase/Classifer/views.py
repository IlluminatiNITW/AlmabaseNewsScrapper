from django.shortcuts import render
from Classifer.models import *
import datetime
# Create your views here.


def homeview(request):
	return render(request,'index.djt',{})


def showcollege(request):
	articles=Article.objects.filter(relevant = True)
	for article in articles:
		article.summary = article.summary[:150]+"..."
	print articles
	response={}
	response['articles']=articles
	response['dtime']=datetime.datetime.now()
	return render(request,'second.djt',response)

