from django.shortcuts import render
from django.http import request,HttpResponse
from .models import Article
# Create your views here.
def index(request):
    obj = Article.objects.get(id=2)
    return HttpResponse(obj.title + obj.desc)
