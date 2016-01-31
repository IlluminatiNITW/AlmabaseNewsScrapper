from django.shortcuts import render
from Classifer.models import *
import datetime
# Create your views here.


def homeview(request):
	return render(request,'index.djt',{})


def showcollege(request):
	articles=Article.objects.all()
	print articles
	response={}
	response['articles']=articles
	response['dtime']=datetime.datetime.now()
	return render(request,'second.djt',response)

