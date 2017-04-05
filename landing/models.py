from django.db import models

# Create your models here.

class alumni(models.Model):
	nama = models.CharField(default='', max_length=200)
	alamat = models.CharField(default="",max_length=300)

