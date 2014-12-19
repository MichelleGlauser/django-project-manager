from django.conf.urls import patterns, include, url
from . import views
from django.conf import settings

if settings.DEBUG:
    urlpatterns = patterns('',
        # url(r'^$', views.show_projects, name='index'),
        # url(r'^project/(?P<pk>[0-9]+)/$', views.create_project),
        url(r'^$', views.list_projects),
    	url(r'^project/(?P<pk>[0-9]+)/$', views.show_project),
    	url(r'^project/new/$', views.create_project),
    	url(r'^task/new/$', views.create_task),
    	url(r'^task/edit/$', views.edit_task),

    )