from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article

def root(request):
    return HttpResponseRedirect('home')

def home(request):
    context = {'date' : datetime.today().strftime('%Y-%m-%d'), 
    'articles': Article.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def article(request, id):
    context = {'article': Article.objects.get(pk=id)} 
    return render(request,'article.html', context)
