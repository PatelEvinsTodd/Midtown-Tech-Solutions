from django.contrib import admin
from public.models import Article, Position, Worker

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Position)
admin.site.register(Worker)
