from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import alumni_model
from .forms import alumni_form
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from dashboard.models import *




def home(request):

    return render(request,"home.html")

def galeri(request):
    judul="GALERI INFORMATIKA"
    subJudul= "Galeri Kegiatan Informatika UMS"
    data_gallery = gallery_model.objects.all().order_by(-timestamp)
    context={

        'judul':judul,
        'subJudul':subJudul,
        'gallery':data_gallery,
    }
    return render(request,"berita/galeri.html",context)

def berita(request):
    judul="Berita"
    subJudul= "Kabar Keadaan Terbaru Prodi Informatika"
    context={
        'judul':judul,
        'subJudul':subJudul,
    }
    return render(request,"berita/berita.html",context)

def pengumuman(request):
    judul="Pengumuman"
    subJudul= "Kabar Keadaan Terbaru Prodi Informatika"
    context={
        'judul':judul,
        'subJudul':subJudul,
    }
    return render(request,"berita/pengumuman.html",context)

def kurikulum(request):
    data_kurikulum = kurikulum_models.objects.all()
    judul="KURIKULUM INFORMATIKA"
    subJudul= "Kurikulum Program Studi Informatika"
    context={
        'judul':judul,
        'subJudul':subJudul,
        'kurikulum':data_kurikulum,
    }
    return render(request,"kurikulum/kurikulum.html",context)

def profil(request):
    judul="PROFIL INFORMATIKA"
    subJudul= ""
    context={
        'judul':judul,
    }
    return render(request,"profil/profil.html",context)

def identitas(request):
    judul = "TENTANG INFORMATIKA"
    subJudul= ""
    context={
        'judul':judul,
    }
    return render(request,"profil/identitas.html",context)

def staff(request):
    data_staff = staff_model.objects.all()
    judul = "STAFF PENGAJAR"
    subJudul= ""
    context={
        'judul':judul,
        'staff':data_staff,
    }
    return render(request,"profil/staff.html",context)

def visi(request):
    judul = "VISI DAN MISI"
    subJudul= ""
    context = {
        'judul':judul,
    }
    return render(request,"profil/visi.html",context)

def prestasi(request):
    judul = "PRESTASI INFORMATIKA"
    subJudul= ""
    context={
        'judul':judul,
    }
    return render(request,"profil/prestasi.html",context)

def fosti(request):
    judul = "FOSTI"
    subJudul= "Forum Open Source Informatika"
    context={
        'judul':judul,
        'subJudul':subJudul,
    }
    return render(request,"ukm/fosti.html",context)

def himatif(request):
    judul = "HIMATIF"
    subJudul= "Himpunan Mahasiswa Teknik Informatika"
    context={
        'judul':judul,
        'subJudul':subJudul,
    }
    return render(request,"ukm/himatif.html",context)

def alumni(request):
    form_alumni = alumni_form(request.POST or None)
    if form_alumni.is_valid():
        isi = form_alumni.save(commit=False)
        isi.save()
        messages.success(request,'Terima Kasih anda telah mengisi data alumni. Data anda sudah tersimpan.')
    judul = "MANAJEMEN ALUMNI"
    subJudul= "Alumni ? Daftar Disini"
    context = {
    'form_alumni':form_alumni,
    'judul':judul,
    'subJudul':subJudul,
    }
    return render(request,'alumni/alumni.html',context)




def dashboard(request):
    return render(request,"dashboard/index.html")

'''Berita view'''
def berita_list(request):
    list_berita_list = berita_model.objects.filter(draft=False).filter(tag='Berita').filter(publish__lte=Now())

    #pagination
    page = request.GET.get('page',1)
    paginator = Paginator(list_berita_list, 5)


    try:
        beritas = paginator.page(page)
    except PageNotAnInteger:
        beritas = paginator.page(1)
    except EmptyPage:
        beritas = paginator.page(paginator.num_pages)
    context ={
        'beritas' : beritas,
    }
    query = request.GET.get("q")
    if query:
        list_berita_list = list_berita_list.filter(
            Q(judul__icontains=query)|
            Q(content__icontains=query)
        ).distinct()
        context['beritas'] = list_berita_list
    context['title'] = 'Berita'


    return render(request,"berita/list_berita.html",context)

def pengumuman_list(request):
    list_berita_list = berita_model.objects.filter(draft=False).filter(tag='Pengumuman').filter(publish__lte=Now())

    #pagination
    page = request.GET.get('page',1)
    paginator = Paginator(list_berita_list, 5)


    try:
        beritas = paginator.page(page)
    except PageNotAnInteger:
        beritas = paginator.page(1)
    except EmptyPage:
        beritas = paginator.page(paginator.num_pages)
    context ={
        'beritas' : beritas,
    }
    query = request.GET.get("q")
    if query:
        list_berita_list = list_berita_list.filter(
            Q(judul__icontains=query)|
            Q(content__icontains=query)
        ).distinct()
        context['beritas'] = list_berita_list
    context['title'] = 'Pengumuman'


    return render(request,"berita/list_pengumuman.html",context)


    



