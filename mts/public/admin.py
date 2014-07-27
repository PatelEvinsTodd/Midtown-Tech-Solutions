from django.contrib import admin
from public.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)
