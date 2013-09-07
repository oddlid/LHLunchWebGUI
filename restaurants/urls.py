from django.conf.urls import patterns, url

from restaurants import views

urlpatterns = patterns('',
      #url(r'^$', views.index, name='index')
      url(r'^$', views.formats, name='formats'),
      url(r'lindholmen/', views.index, name='index'),
)
