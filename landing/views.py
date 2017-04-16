from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import alumni_model
from .forms import alumni_form
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from dashboard.models import *
from django.utils import timezone


def home(request):
    return render(request,"home.html")

def galeri(request):
    judul="GALERI INFORMATIKA"
    subJudul= "Galeri Kegiatan Informatika UMS"
    data_gallery = gallery_model.objects.all().order_by('-timestamp')
    page = request.GET.get('page',1)
    paginator = Paginator(data_gallery, 10)


    try:
        galeri = paginator.page(page)
    except PageNotAnInteger:
        galeri = paginator.page(1)
    except EmptyPage:
        galeri = paginator.page(paginator.num_pages)
    context={

        'judul':judul,
        'subJudul':subJudul,
        'galeri':galeri,
    }
    return render(request,"berita/galeri.html",context)

def berita(request):
    # list_berita_list = berita_model.objects.filter(tag='Berita').filter(draft=False).filter(publish__lte=timezone.now())
    list_berita_list = berita_model.objects.filter(draft=False)
    judul="Berita & Pengumuman"
    subJudul= "Kabar Keadaan Terbaru Prodi Informatika"
    #pagination
    page = request.GET.get('page',1)
    paginator = Paginator(list_berita_list, 8)


    try:
        beritas = paginator.page(page)
    except PageNotAnInteger:
        beritas = paginator.page(1)
    except EmptyPage:
        beritas = paginator.page(paginator.num_pages)
    context ={
        'beritas' : beritas,
        'subJudul':subJudul,
    }
    query = request.GET.get("q")
    if query:
        list_berita_list = list_berita_list.filter(
            Q(judul__icontains=query)|
            Q(content__icontains=query)
        ).distinct()
        context['beritas'] = list_berita_list
    context['judul'] = judul
    return render(request,"berita/berita.html",context)

def detail_berita(request,slug=None):
    data = get_object_or_404(berita_model,slug=slug)
    context={
    'obj':data,
    'judul':'Detail Berita',
    }

    return render(request,"berita/berita-detail.html",context)

def pengumuman(request):
<<<<<<< HEAD
    list_pengumuman_list = berita_model.objects.filter(tag='Pengumuman').filter(draft=False).filter(publish__lte=timezone.now())
=======
    list_pengumuman_list = berita_model.objects.filter(draft=False).filter(tag='Pengumuman')
>>>>>>> remotes/fikrikhaidir/informatika-web/master
    judul="Pengumuman"
    subJudul= "Kabar Keadaan Terbaru Prodi Informatika"
    #pagination
    page = request.GET.get('page',1)
    paginator = Paginator(list_pengumuman_list, 8)


    try:
        beritas = paginator.page(page)
    except PageNotAnInteger:
        beritas = paginator.page(1)
    except EmptyPage:
        beritas = paginator.page(paginator.num_pages)
    context ={
        'beritas' : beritas,
        'judul':judul,
        'subJudul':subJudul,
    }
    query = request.GET.get("q")
    if query:
        list_pengumuman_list = list_pengumuman_list.filter(
            Q(judul__icontains=query)|
            Q(content__icontains=query)
        ).distinct()
        context['beritas'] = list_pengumuman_list
    context['title'] = 'Pengumuman'

    return render(request,"berita/pengumuman.html",context)

def detail_pengumuman(request,slug=None):
    data_pengumuman = get_object_or_404(berita_model,slug=slug)
    context={
    'obj':data_pengumuman,
    'judul':'Detail Pengumuman',
    }

    return render(request,"berita/pengumuman-detail.html",context)

def kurikulum(request):
    data_kurikulum = kurikulum_model.objects.all().order_by('-semester')
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
    data_staff = staff_model.objects.filter(posisi='staff')
    data_dosen_tetap = staff_model.objects.filter(posisi='dosen tetap')
    data_dosen_profesi = staff_model.objects.filter(posisi='dosen profesi')
    judul = "STAFF PENGAJAR"
    subJudul= ""
    context={
        'judul':judul,
        'staff':data_staff,
        'dosen_tetap':data_dosen_tetap,
        'dosen_profesi':data_dosen_profesi,
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
    data = ukm_model.objects.all()
    context={
        'judul':judul,
        'subJudul':subJudul,
        'fosti':data,
    }
    return render(request,"ukm/fosti.html",context)

def himatif(request):
    judul = "HIMATIF"
    subJudul= "Himpunan Mahasiswa Teknik Informatika"
    data = ukm_model.objects.all()
    context={
        'judul':judul,
        'subJudul':subJudul,
        'himatif':data,
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

@login_required()
def dashboard(request):
    return render(request,"dashboard/index.html")

def dokumen(request):
    data_dokumen = dokumen_model.objects.all()
    context = {
    'dokumen':data_dokumen,
    'judul':'Data Dokumen',
    }
    return render(request,'dokumen/dokumen.html',context)

def dokumen_detail(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data = get_object_or_404(dokumen_model,id=id)
    context={
    'obj':data,
    'judul':'Dokumen',
    }
    return render(request,'dokumen/dokumen.html',context)
