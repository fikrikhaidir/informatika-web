from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^galeri/$', views.galeri, name='galeri'),
    url(r'^profil/informatika/$', views.profil, name='profil'),
    url(r'^profil/identitas/$', views.identitas, name='identitas'),
    url(r'^profil/staff/$', views.staff, name='staff'),
    url(r'^profil/visi/$', views.visi, name='visi'),
    url(r'^profil/prestasi/$', views.prestasi, name='prestasi'),
    url(r'^kurikulum/$', views.kurikulum, name='kurikulum'),
    url(r'^ukm/fosti/$', views.fosti, name='fosti'),
    url(r'^ukm/himatif/$', views.himatif, name='himatif'),
    url(r'^alumni/$', views.alumni, name='alumni'),

]
