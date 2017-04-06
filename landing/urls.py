from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import alumni_dashboard
from django.conf.urls import include,url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profil/$', views.profil, name='profil'),
    url(r'^kurikulum/$', views.kurikulum, name='kurikulum'),
    url(r'^ukm/$', views.ukm, name='ukm'),
    url(r'^alumni/$', views.alumni, name='alumni'),

    url(r'^rekapan/$',views.cetak_rekapan_alumni, name='cetak_alumni'),
    url(r'^data_alumni/$',alumni_dashboard, name='alumni_dashboard'),

    # url(r'^berita/$', views.listBerita, name='berita'),
    # url(r'^adm/detail_berita/(?P<id>\d+)/$', views.detail_berita, name='detail_berita'),
    # url(r'^timeline/$', views.view_timeline, name='timeline'),

    url(r'^captcha/', include('captcha.urls')),

]
