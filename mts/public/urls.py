from django.conf.urls import patterns, url
import public.views

urlpatterns = patterns('',
    url(r'^$', public.views.index, name="index"),
    url(r'^about$', public.views.about, name="about"),
    url(r'^organization$', public.views.people, name="people"),
    url(r'^contact$', public.views.contact, name="contact"),
)
