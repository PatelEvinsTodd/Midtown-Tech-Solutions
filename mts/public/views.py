from django.shortcuts import render

from public.models import Article

def index(request):
    context = {}
    return render(request, 'public/base.html', context)
