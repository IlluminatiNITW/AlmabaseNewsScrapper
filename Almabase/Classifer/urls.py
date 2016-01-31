from django.conf.urls import include, url
from Classifer import views

urlpatterns = [
    
    url(r'^$', views.homeview),
    url(r'^showcollege/$', views.showcollege),
]

