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

def article_create(request):
    context = {
        'title': None,
        'description': None,
        'status': None
    }
    if request.POST:
        article_obj = Article(title=request.POST['title'],desc=request.POST['desc'])
        context = {
            'title': request.POST['title'],
            'description': request.POST['desc'],
            'status': 'created'
        }
        article_obj.save()
    return render(request,'create.html',context)

def article_search(request):
    context = {
        'article': None,
    }
    if request.GET:
        try:
            int_query = int(request.GET['q'])
            article_obj = Article.objects.get(id=int_query)
            context = {
                'article': article_obj
            }
        except:
            pass
    return render(request,'search.html',context)
