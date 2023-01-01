from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('<int:id>',article_details),
    path('create',article_create),
    path('search',article_search)
]