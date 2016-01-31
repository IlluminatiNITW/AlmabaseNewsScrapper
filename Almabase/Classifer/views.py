from django.shortcuts import render

# Create your views here.


def homeview(request):
	return render(request,'index.djt',{})


def showcollege(request):
	return render(request,'second.djt',{})

