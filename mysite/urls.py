from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    # url(r'^base/', views.base),
    url(r'^article/(?P<article_id>[0-9])/$', views.showContent, name='showContent')


]