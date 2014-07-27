from django.conf.urls import patterns, url
import public.views

urlpatterns = patterns('',
    url(r'^$', public.views.index, name="index"),
)
