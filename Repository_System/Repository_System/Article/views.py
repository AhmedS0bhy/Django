from django.shortcuts import render
from django.http import request,HttpResponse
from .models import Article
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    obj = Article.objects.get(id=1)
    context = {
        "id": obj.id,
        "title": obj.title,
        "desc": obj.desc,
    }
    return HttpResponse(render_to_string('home.html', context))
