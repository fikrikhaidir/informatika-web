from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.conf import settings
from PIL import Image as img
# import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.

class berita_model(models.Model):
	judul = models.CharField(default='', max_length=200)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='upload/berita', default='', blank=True)
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


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.judul)
#     if new_slug is not None:
#         slug = new_slug
#     qs = berita.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_berita_receiver(sender,instance,*args,**kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)

# pre_save.connect(pre_save_berita_receiver,sender=berita)

class staff_model(models.Model):
	nama = models.CharField(default='',null=False,max_length=20)
	nidn = models.CharField(default='',null=False,max_length=10)
	jabatan = models.CharField(default='',null=False,max_length=30)
	gelar = models.CharField(default='',null=False,max_length=30)
	pendidikan1 = models.CharField(default='',null=False,max_length=30)
	pendidikan2 = models.CharField(default='',blank=True,max_length=30)
	pendidikan3 = models.CharField(default='',blank=True,max_length=30)
	bidang_keahlian1 = models.CharField(default='',null=False,max_length=50)
	bidang_keahlian2 = models.CharField(default='',blank=True,max_length=50)
	bidang_keahlian3 = models.CharField(default='',blank=True,max_length=50)
	foto = models.ImageField(upload_to='upload/dosen',default='',blank=True)

	# def save(self,*args,**kwargs):
	# 	if self.foto:
	# 		image = img.open(StringIO.StringIO(self.foto.read()))
	# 		image.thumbnail((100,80),img.ANTIALIAS)
	# 		output = StringIO.StringIO()
	# 		image.save(output,format='JPEG',quality=75)
	# 		output.seek(0)
	# 		self.foto=InMemoryUploadedFile(output,'ImageField',"%s.jpg" %self.foto.nama,  'image/jpeg', output.len, None)
	# 	super(staff_model,self).save(*args,**kwargs)

	def __str__(self):
		return self.nama


class gallery_model(models.Model):
	judul = models.CharField(default='',null=False,max_length=20)
	caption = models.CharField(default='',null=False,max_length=300)
	image = models.ImageField(upload_to='upload/gallery',default='',blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.judul

	class Meta:
		ordering = ["-timestamp"]
	

