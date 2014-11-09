from django.conf.urls import patterns, include, url
from Picture import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
  url(r'^form/$', TemplateView.as_view(template_name = "Picture/index.html"), name='formurl'),
  url(r'^handledata/$', views.HandleData.as_view(), name='handledata'),
  url(r'^delete/(?P<pictureKey>\d+)/$', views.Delete.as_view(), name='delete'), 
  url(r'^list/$', views.List.as_view(template_name = "Picture/list.html"), name='list'),
  url(r'^thumbnail/$', views.List.as_view(template_name = "Picture/thumbnail.html"), name="thumbnail"),
)