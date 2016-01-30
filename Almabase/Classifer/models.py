from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
	title=models.CharField(max_length=180)
	summary=models.TextField()
	url=models.CharField(max_length=300)
	author=models.CharField(max_length=300)
	college=models.CharField(max_length=300,default="NITW")
	relevant=models.BooleanField(default=True)
	def __unicode__(self):
		return self.title

class KeywordList(models.Model):
	keyword=models.CharField(max_length=300)
	def __unicode__(self):
		return self.keyword
    
class Keywords(models.Model):
	article=models.OneToOneField(Article)
	keywords=models.ManyToManyField(KeywordList,blank=True)
	def __unicode__(self):
		return self.article.title
    

