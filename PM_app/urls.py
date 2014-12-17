from django.conf.urls import patterns, include, url
from <appfoldername> import views
from django.conf import settings

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^$', views.index, name='index')
    )