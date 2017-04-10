from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class alumni_model(models.Model):
	nama = models.CharField(default='', max_length=200,verbose_name='Nama Lengkap')
	nim = models.CharField(default='', max_length=10,verbose_name='NIM')
	konsentrasi = models.CharField(default='', max_length=30,verbose_name='Konsentrasi')
	tempat_kerja = models.CharField(default='', max_length=100,verbose_name='Nama Perusahaan')
	jabatan = models.CharField(default='', max_length=100,verbose_name='Posisi Pekerjaan')
	tahun_masuk = models.PositiveIntegerField(default='',null=False,validators=[MaxValueValidator(9999)],verbose_name='Tahun Masuk')
	tahun_keluar = models.PositiveIntegerField(default='',null=False,validators=[MaxValueValidator(9999)],verbose_name='Tahun Keluar')

	def __unicode__(self):
		return '%s'% self.nama




