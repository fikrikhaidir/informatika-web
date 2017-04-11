from django.conf.urls import url, include
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^berita/berita/$', views.berita, name='berita'),
    url(r'^berita/pengumuman/$', views.pengumuman, name='pengumuman'),
    url(r'^berita/galeri/$', views.galeri, name='galeri'),
    url(r'^profil/informatika/$', views.identitas, name='profil'),
    url(r'^profil/identitas/$', views.identitas, name='identitas'),
    url(r'^profil/staff/$', views.staff, name='staff'),
    url(r'^profil/visi/$', views.visi, name='visi'),
    url(r'^profil/prestasi/$', views.prestasi, name='prestasi'),
    url(r'^kurikulum/$', views.kurikulum, name='kurikulum'),
    url(r'^ukm/fosti/$', views.fosti, name='fosti'),
    url(r'^ukm/himatif/$', views.himatif, name='himatif'),
    url(r'^alumni/$', views.alumni, name='alumni'),

    url(r'^login/$', views.login_admin, name='login'),




    # url(r'^berita/$', views.listBerita, name='berita'),
    # url(r'^adm/detail_berita/(?P<id>\d+)/$', views.detail_berita, name='detail_berita'),
    # url(r'^timeline/$', views.view_timeline, name='timeline'),




]
