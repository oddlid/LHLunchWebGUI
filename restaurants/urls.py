from django.conf.urls import patterns, url

from restaurants import views

urlpatterns = patterns('',
      url(r'^$', views.index, name='index')
)
