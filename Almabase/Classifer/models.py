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
	addedat=models.DateTimeField(auto_now=True)
	image_link = models.CharField(max_length=300,default = "http://menengage.org/wp-content/uploads/2013/11/news-default.png")

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
    

class Person(models.Model):
	name = models.CharField(max_length= 100)
	link = models.CharField(max_length=100, default="http://www.nitwaa.in/")
	def __unicode__(self):
		return self.name

class PersonList(models.Model):
	article=models.OneToOneField(Article)
	persons=models.ManyToManyField(Person,blank=True)
	def __unicode__(self):
		return self.article.title

class Organization(models.Model):
	name = models.CharField(max_length= 100)
	link = models.CharField(max_length=100, default="http://www.nitwaa.in/")
	def __unicode__(self):
		return self.name

class OrganizationList(models.Model):
	article=models.OneToOneField(Article)
	orgs=models.ManyToManyField(Organization,blank=True)
	def __unicode__(self):
		return self.article.title
