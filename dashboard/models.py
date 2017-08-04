from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.conf import settings
from stdimage.models import StdImageField
from stdimage.validators import MaxSizeValidator
from django.core.validators import MaxValueValidator
# from PIL import Image as img
# import io
# from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.

class berita_model(models.Model):
	judul = models.CharField(default='', max_length=200)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	slug = models.SlugField(unique=True)
	image = StdImageField(upload_to='upload/berita',validators=[MaxSizeValidator(1300, 1300)],blank=True)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	tag = models.CharField(default='',null=False,max_length=20)

	def __str__(self):
	    return self.judul

	class Meta:
	    ordering = ["-updated"]

	def get_absolute_url(self):
	    return reverse("dashboard:detail_berita", kwargs={"slug": self.slug})

    # def get_markdown(self):
    #     content = self.content
    #     markdown_text = markdown(content)
    #     return mark_safe(markdown_text)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.judul)
    if new_slug is not None:
        slug = new_slug
    qs = berita_model.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_berita_model_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_berita_model_receiver,sender=berita_model)

class staff_model(models.Model):
	nama = models.CharField(default='',null=False,max_length=20,verbose_name='Nama Lengkap')
	nama_display = models.CharField(default='',null=False,max_length=14,verbose_name='Nama yang Ditampilkan')
	nidn = models.CharField(default='',null=False,max_length=10,verbose_name='NIDN')
	jabatan = models.CharField(default='',null=False,max_length=30,verbose_name='Jabatan Akademik')
	gelar1 = models.CharField(default='',null=False,max_length=30,verbose_name='Gelar Pendidikan S1')
	gelar2 = models.CharField(default='',blank=True,max_length=30,verbose_name='Gelar Pendidikan S2')
	gelar3 = models.CharField(default='',blank=True,max_length=30,verbose_name='Gelar Pendidikan S3')
	pendidikan1 = models.CharField(default='',null=False,max_length=100,verbose_name='Universitas Jenjang SI')
	pendidikan2 = models.CharField(default='',blank=True,max_length=100,verbose_name='Universitas Jenjang S2')
	pendidikan3 = models.CharField(default='',blank=True,max_length=100,verbose_name='Universitas Jenjang S3')
	bidang_keahlian1 = models.CharField(default='',null=False,max_length=80,verbose_name='Bidang Keahlian S1')
	bidang_keahlian2 = models.CharField(default='',blank=True,max_length=80,verbose_name='Bidang Keahlian S2')
	bidang_keahlian3 = models.CharField(default='',blank=True,max_length=80,verbose_name='Bidang Keahlian S3')
	penelitian = models.CharField(default='',blank=True,max_length=200,verbose_name='Penelitian Google Scholar')
	biografi = models.TextField(default='',blank=True,verbose_name='Biografi')
	foto = StdImageField(upload_to='upload/dosen',validators=[MaxSizeValidator(1028, 768)],blank=True)
	posisi = models.CharField(default='',null=False,max_length=30)

	def save(self,*args,**kwargs):
		nama = self.nama_display.upper()
		if self.nama_display:
			self.nama_display = nama
		super(staff_model,self).save(*args,**kwargs)

	def __unicode__(self):
		return '%s' % self.nama


class gallery_model(models.Model):
	judul = models.CharField(default='',null=False,max_length=20,verbose_name='Judul Foto')
	caption = models.CharField(default='',null=False,max_length=300,verbose_name='Caption Foto')
	image = StdImageField(upload_to='upload/gallery',validators=[MaxSizeValidator(1028, 768)],verbose_name='Foto',blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return '%s' % self.judul

	class Meta:
		ordering = ["-timestamp"]


class kurikulum_model(models.Model):
	semester = models.PositiveIntegerField(default='',null=False,validators=[MaxValueValidator(9)],verbose_name='Semester')
	makul = models.CharField(default='',null=False,max_length=40,verbose_name='Nama Mata Kuliah')
	kode = models.CharField(default='',null=False,max_length=10,verbose_name='Kode MK')
	sks = models.PositiveIntegerField(default='',null=False,validators=[MaxValueValidator(9)],verbose_name='SKS')
	wajib = models.BooleanField(default='False',verbose_name='Mata Kuliah Wajib/Pilihan (*Jika Wajib Dicentang)')

	def __unicode__(self):
		return '%s' % self.makul

class dokumen_model(models.Model):
	deskripsi = models.CharField(default='',max_length=30,verbose_name='Nama Dokumen')
	file = models.FileField(upload_to="upload/document",blank=True,verbose_name='File')
	keterangan = models.TextField(verbose_name='Deskripsi')
	tanggal = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s' % self.keterangan

class ukm_model(models.Model):
	link_fosti = models.CharField(default='',null=False,verbose_name='Link FOSTI',max_length=300)
	link_himatif = models.CharField(default='',null=False,verbose_name='Link HIMATIF',max_length=300)

	def __unicode__(self):
		return '%s' % self.link_fosti
