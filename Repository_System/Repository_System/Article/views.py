from django.shortcuts import render
from django.http import request,HttpResponse
from .models import Article
# Create your views here.
def home(request):
    obj = Article.objects.all()
    context = {
        'articles': obj
    }
    return HttpResponse(render(request,'home.html',context))

def article_details(request,id=None):
    article_obj = Article.objects.get(id=id)
    context = {
        'article': article_obj
    }
    return HttpResponse(render(request,'article.html',context))