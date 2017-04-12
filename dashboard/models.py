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
	image = StdImageField(upload_to='upload/berita',validators=[MaxSizeValidator(1028, 768)],blank=True)
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


def pre_save_berita_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_berita_receiver,sender=berita_model)

class staff_model(models.Model):
	nama = models.CharField(default='',null=False,max_length=20,verbose_name='Nama Lengkap')
	nama_display = models.CharField(default='',null=False,max_length=14,verbose_name='Nama yang Ditampilkan')
	nidn = models.CharField(default='',null=False,max_length=10,verbose_name='NIDN')
	jabatan = models.CharField(default='',null=False,max_length=30,verbose_name='Jabatan Akademik')
	gelar1 = models.CharField(default='',null=False,max_length=30,verbose_name='Gelar Pendidikan S1')
	gelar2 = models.CharField(default='',null=False,max_length=30,verbose_name='Gelar Pendidikan S2')  
	gelar3 = models.CharField(default='',null=False,max_length=30,verbose_name='Gelar Pendidikan S3') 
	pendidikan1 = models.CharField(default='',null=False,max_length=30,verbose_name='Universitas Jenjang SI')
	pendidikan2 = models.CharField(default='',blank=True,max_length=30,verbose_name='Universitas Jenjang S2')
	pendidikan3 = models.CharField(default='',blank=True,max_length=30,verbose_name='Universitas Jenjang S3')
	bidang_keahlian1 = models.CharField(default='',null=False,max_length=50,verbose_name='Bidang Keahlian S1')
	bidang_keahlian2 = models.CharField(default='',blank=True,max_length=50,verbose_name='Bidang Keahlian S2')
	bidang_keahlian3 = models.CharField(default='',blank=True,max_length=50,verbose_name='Bidang Keahlian S3')
	penelitian = models.CharField(default='',blank=True,max_length=100,verbose_name='Penelitian Google Scholar')
	biografi = models.TextField(default='',blank=True,verbose_name='Biografi')
	foto = StdImageField(upload_to='upload/dosen',validators=[MaxSizeValidator(1028, 768)],blank=True)


	# def save(self,*args,**kwargs):
	# 	if self.foto:
	# 		image = img.open(io.StringIO(self.foto.read()))
	# 		image.thumbnail((100,80),img.ANTIALIAS)
	# 		output = io.StringIO()
	# 		image.save(output,format='JPEG',quality=75)
	# 		output.seek(0)
	# 		self.foto=InMemoryUploadedFile(output,'ImageField',"%s.jpg" %self.foto.nama,  'image/jpeg', output.len, None)
	# 	super(staff_model,self).save(*args,**kwargs)

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
	kode = models.CharField(default='',null=False,max_length=5,verbose_name='Kode MK')
	sks = models.PositiveIntegerField(default='',null=False,validators=[MaxValueValidator(9)],verbose_name='SKS')
	wajib = models.BooleanField(default='False',verbose_name='Mata Kuliah Wajib/Pilihan (*Jika Wajib Dicentang)')

	def __unicode__(self):
		return '%s' % self.makul

class beranda_model(models.Model):
	judul_besar = models.CharField(default='',max_length=100,null=False,verbose_name='Judul Tagline')
	keterangan_singkat = models.CharField(default='',max_length=200,null=False,verbose_name='Keterangan Singkat')
	nama_button = models.CharField(default='',max_length=50,null=False,verbose_name='Nama Button')
	link_button = models.CharField(default='',max_length=400,null=False,verbose_name='Link Button')
	foto = StdImageField(upload_to='upload/beranda',validators=[MaxSizeValidator(4300, 2850)],verbose_name='Foto(Maks : 4300px X 2850px)',blank=True)
	tampil = models.BooleanField(default=False,verbose_name='Ditampilkan')

	def save(self,*args,**kwargs):
		judul = self.judul_besar.upper()
		keterangan = self.keterangan_singkat.upper()
		button = self.nama_button.upper()
		if self.judul_besar :
			self.judul_besar = judul
			self.keterangan_singkat = keterangan
			self.nama_button = button
		super(beranda_model,self).save(*args,**kwargs)


	def __unicode__(self):
		return '%s' % self.judul_besar
