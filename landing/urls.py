from django.conf.urls import url, include
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profil/$', views.profil, name='profil'),
    url(r'^identitas/$', views.identitas, name='identitas'),
    url(r'^staff/$', views.staff, name='staff'),
    url(r'^visi/$', views.visi, name='visi'),
    url(r'^kurikulum/$', views.kurikulum, name='kurikulum'),
    url(r'^ukm/$', views.ukm, name='ukm'),
    url(r'^alumni/$', views.alumni, name='alumni'),

    

    # url(r'^berita/$', views.listBerita, name='berita'),
    # url(r'^adm/detail_berita/(?P<id>\d+)/$', views.detail_berita, name='detail_berita'),
    # url(r'^timeline/$', views.view_timeline, name='timeline'),

   

]
