from django.conf.urls import patterns, include, url
from Picture import views

urlpatterns = patterns('',
  url(r'^form/$', views.formview, name='formurl'),
  url(r'^handledata/$', views.handledata, name='handledata'),
  url(r'^delete/(\d+)/$', views.delete, name='delete'), 
  url(r'^list/$', views.list, name='list'),
  url(r'^thumbnail/$', views.thumbnail, name="thumbnail"),
)