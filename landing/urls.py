from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^berita/$', views.listBerita, name='berita'),
    # url(r'^adm/detail_berita/(?P<id>\d+)/$', views.detail_berita, name='detail_berita'),
    # url(r'^timeline/$', views.view_timeline, name='timeline'),

]
