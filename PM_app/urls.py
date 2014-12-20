from django.conf.urls import patterns, include, url
from . import views
from django.conf import settings

if settings.DEBUG:
    urlpatterns = patterns('',
        # url(r'^$', views.show_projects, name='index'),
        # url(r'^project/(?P<pk>[0-9]+)/$', views.create_project),
        url(r'^$', views.list_projects, name='list_projects'),
    	url(r'^project/(?P<project_pk>[0-9]+)/$', views.show_project, name='show_project'),
    	url(r'^project/new/$', views.create_project, name='create_project'),
    	url(r'^project/(?P<project_pk>[0-9]+)/task/new/$', views.create_task, name='create_task'),
    	url(r'^project/(?P<project_pk>[0-9]+)/task/(?P<task_pk>[0-9]+)/edit/$', views.edit_task, name='edit_task'),
    	# url(r'^task/edit/$', TaskUpdate.as_view()),
    )