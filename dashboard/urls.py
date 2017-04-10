from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^dashboard/rekapan/$',views.cetak_rekapan_alumni, name='cetak_alumni'),
url(r'^dashboard/data_alumni/$',views.alumni_dashboard, name='alumni_dashboard'),
url(r'^dashboard/staff/$',views.staff, name='staff'),
url(r'^dashboard/tambah_staff/$',views.staff_tambah, name='tambah_staff'),
url(r'^dashboard/edit_staff/$',views.staff_edit, name='edit_staff'),
url(r'^dashboard/staff/(?P<id>\d+)/$', views.staff_detail, name='detail_staff'),
url(r'^dashboard/hapus_staff/(?P<id>\d+)/$',views.staff_hapus, name='hapus_staff'),
url(r'^dashboard/gallery/$',views.gallery, name='gallery'),
url(r'^dashboard/tambah_gallery/$',views.gallery_tambah, name='tambah_gallery'),
url(r'^dashboard/edit_gallery/$',views.gallery_edit, name='edit_gallery'),
url(r'^dashboard/hapus_gallery/$',views.gallery_hapus, name='hapus_gallery'),
url(r'^dashboard/tambah_berita/$',views.berita_tambah, name='tambah_berita'),
url(r'^dashboard/edit_berita/$',views.berita_edit, name='edit_berita'),
url(r'^dashboard/hapus_berita/$',views.berita_hapus, name='hapus_berita'),
url(r'^dashboard/berita/$',views.list_berita, name='berita'),
url(r'^dashboard/pengumuman/$',views.list_pengumuman, name='pengumuman'),
] 