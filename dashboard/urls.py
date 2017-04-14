from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^dashboard/rekapan/$',views.cetak_rekapan_alumni, name='cetak_alumni'),
url(r'^dashboard/data_alumni/$',views.alumni_dashboard, name='alumni_dashboard'),
url(r'^dashboard/staff/$',views.staff, name='staff'),
url(r'^dashboard/tambah_staff/$',views.staff_tambah, name='tambah_staff'),
url(r'^dashboard/edit_staff/(?P<id>\d+)/$',views.staff_edit, name='edit_staff'),
url(r'^dashboard/hapus_staff/(?P<id>\d+)/$',views.staff_hapus, name='hapus_staff'),
url(r'^dashboard/gallery/$',views.gallery, name='gallery'),
url(r'^dashboard/gallery/tambah_gallery/$',views.gallery_tambah, name='tambah_gallery'),
url(r'^dashboard/gallery/edit_gallery/(?P<id>\d+)/$',views.gallery_edit, name='edit_gallery'),
url(r'^dashboard/gallery/hapus_gallery/(?P<id>\d+)/$',views.gallery_hapus, name='hapus_gallery'),
url(r'^dashboard/berita/tambah_berita/$',views.berita_tambah, name='tambah_berita'),
url(r'^dashboard/pengumuman/tambah_pengumuman/$',views.pengumuman_tambah, name='tambah_pengumuman'),
url(r'^dashboard/berita/edit_berita/(?P<slug>[\w-]+)/$',views.berita_edit, name='edit_berita'),
url(r'^dashboard/pengumuman/edit_pengumuman/(?P<slug>[\w-]+)/$',views.pengumuman_edit, name='edit_pengumuman'),
url(r'^dashboard/berita/hapus_berita/(?P<slug>[\w-]+)/$',views.berita_hapus, name='hapus_berita'),
url(r'^dashboard/berita/$',views.list_berita, name='berita'),
url(r'^dashboard/berita/(?P<slug>[\w-]+)/$',views.berita_detail,name='detail_berita'),
url(r'^dashboard/pengumuman/$',views.list_pengumuman, name='pengumuman'),
url(r'^dashboard/kurikulum/$',views.kurikulum, name='kurikulum'),
url(r'^dashboard/tambah_kurikulum/$',views.kurikulum_tambah, name='tambah_kurikulum'),
url(r'^dashboard/edit_kurikulum/(?P<id>\d+)/$',views.kurikulum_edit, name='edit_kurikulum'),
url(r'^dashboard/hapus_kurikulum/(?P<id>\d+)/$',views.kurikulum_hapus, name='hapus_kurikulum'),
<<<<<<< HEAD
url(r'^login/$', views.login_view, name='login'),
url(r'^logout/$', views.logout_view, name='logout'),
url(r'^dashboard/passwords/$', views.password_ubah, name='password'),
url(r'^dashboard/beranda/$', views.beranda, name='beranda'),
url(r'^dashboard/detail_beranda/(?P<id>\d+)/$', views.beranda_detail, name='detail_beranda'),
url(r'^dashboard/buat_beranda/$', views.beranda_buat, name='buat_beranda'),
url(r'^dashboard/edit_beranda/(?P<id>\d+)/$', views.beranda_edit, name='edit_beranda'),
url(r'^dashboard/hapus_beranda/(?P<id>\d+)/$', views.beranda_hapus, name='hapus_beranda'),
] 
=======

url(r'^dashboard/umum/$',views.umum, name='umum'),
]
>>>>>>> remotes/fikrikhaidir/informatika-web/master
