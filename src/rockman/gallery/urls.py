from django.conf.urls import patterns, url
from rockman.gallery import views

urlpatterns = patterns('',

    # url(r'^$', views.index, name='index'),
    url(r'^$', views.gallery, name='gallery'),
)