from django.shortcuts import render

from public.models import Article

def index(request):
    context = {}
    return render(request, 'public/index.html', context)

def about(request):
    context = {}
    return render(request, 'public/about.html', context)

def people(request):
    context = {}
    return render(request, 'public/people.html', context)

def contact(request):
    context = {}
    return render(request, 'public/contact.html', context)
