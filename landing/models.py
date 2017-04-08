from django.db import models


# Create your models here.

class alumni_model(models.Model):
	nama = models.CharField(default='', max_length=200)
	nim = models.CharField(default='', max_length=10)
	konsentrasi = models.CharField(default='', max_length=30)
	pekerjaan = models.CharField(default='', max_length=100)
	jabatan = models.CharField(default='', max_length=100)

	def __str__(self):
		return self.nama




