from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from django.utils.safestring import mark_safe

# Create your models here.

class alumni(models.Model):
	nama = models.CharField(default='', max_length=200)
	alamat = models.CharField(default="",max_length=300)


# class berita(model.Models):
# 	judul = models.CharField(default='', max_length=200)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
#     slug = models.SlugField(unique=True)
#     image = models.ImageField(upload_to='upload/berita', default='', blank=True)
#     content = models.TextField()
#     draft = models.BooleanField(default=False)
#     publish = models.DateField(auto_now=False, auto_now_add=False)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
#     tag = models.CharField(default='',null=False,max_length=20)

#     def __unicode__(self):
#         return '%s' % self.judul

#     class Meta:
#         ordering = ["-updated"]

#     def get_absolute_url(self):
#         return reverse("dashboard:detail_berita", kwargs={"slug": self.slug})

#     # def get_markdown(self):
#     #     content = self.content
#     #     markdown_text = markdown(content)
#     #     return mark_safe(markdown_text)


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

