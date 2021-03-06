# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Classifer', '0006_article_addedat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(default='http://www.nitwaa.in/', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(default='http://www.nitwaa.in/', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='image_link',
            field=models.CharField(default='http://menengage.org/wp-content/uploads/2013/11/news-default.png', max_length=300),
        ),
        migrations.AddField(
            model_name='personlist',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Classifer.Article'),
        ),
        migrations.AddField(
            model_name='personlist',
            name='persons',
            field=models.ManyToManyField(blank=True, to='Classifer.Person'),
        ),
        migrations.AddField(
            model_name='organizationlist',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Classifer.Article'),
        ),
        migrations.AddField(
            model_name='organizationlist',
            name='orgs',
            field=models.ManyToManyField(blank=True, to='Classifer.Organization'),
        ),
    ]
