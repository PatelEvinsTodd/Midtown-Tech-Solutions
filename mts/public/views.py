from django.shortcuts import render

from public.models import Article, Worker

def index(request):
    context = {}
    return render(request, 'public/index.html', context)

def about(request):
    context = {}
    return render(request, 'public/about.html', context)

def people(request):
    workers = Worker.objects.all()
    template_workers = []
    for w in workers:
        tw = {}
        tw["first_name"] = w.first_name
        tw["last_name"] = w.last_name
        tw["position"] = w.position.title
        tw["bio"] = w.bio
        template_workers.append(tw)
    context = {
        "people": template_workers,
    }
    return render(request, 'public/people.html', context)

def contact(request):
    context = {}
    return render(request, 'public/contact.html', context)
