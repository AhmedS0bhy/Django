from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
    search_fields = ["title"]
# Register your models here.
admin.site.register(Article,ArticleAdmin)