from django.shortcuts import render
from .models import berita_model,gallery_model,staff_model
from landing.models import alumni_model
from .forms import staff_form,berita_form,gallery_form
from django.shortcuts import get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages


'''Keperluan Cetak'''
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors

# Create your views here.

def alumni_dashboard(request):
    data_alumni = alumni_model.objects.all()
    context = {
    'data_alumni':data_alumni,
    'title':'Data Alumni',
    }
    return render(request,"dashboard/alumni.html",context)

def cetak_rekapan_alumni(request):
    # if not request.user.is_staff and not request.user.is_superuser:
    #     raise Http404
    # pengaturan respon berformat pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rekapan_alumni.pdf"'

    # mengambil daftar kehadiran dan mengubahnya menjadi data ntuk tabel
    data = alumni_model.objects.all()
    table_data = []
    table_data.append([ "NO","Nama","NIM","Konsentrasi","Pekerjaan","Posisi/Jabatan" ])
    i = 1
    for x in data:
        table_data.append([ i,x.nama, x.nim, x.konsentrasi, x.pekerjaan,x.jabatan ])
        i+=1


    # membuat dokumen baru
    doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()

    # pengaturan tabel di pdf
    table_style = TableStyle([
                               ('ALIGN',(1,1),(-2,-2),'LEFT'),
                               ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('VALIGN',(0,0),(0,-1),'TOP'),
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])
    pendaftar_table = Table(table_data)
    pendaftar_table.setStyle(table_style)

    # mengisi pdf
    content = []
    content.append(Paragraph('Daftar Rekapan Mahasiswa Alumni Informatika', styles['Title']))
    content.append(Spacer(1,12))
    content.append(Paragraph('Berikut ini adalah rekapannya' , styles['Normal']))
    content.append(Spacer(1,12))
    content.append(pendaftar_table)
    content.append(Spacer(1,36))
    # content.append(Paragraph('Mengetahui, ', styles['Normal']))
    # content.append(Spacer(1,48))
    # content.append(Paragraph('Wakil Dekan III ', styles['Normal']))

    # menghasilkan pdf untk di download
    doc.build(content)
    return response

def staff(request):
    data_staff = staff_model.objects.all()
    context={
    'staff':data_staff,
    'judul':'Staff',
    }
    return render(request,'dashboard/staff/list_staff.html',context)

def staff_detail(request,id=None):
    detail = get_object_or_404(staff_model,id=id)
    context={
    'staff_detail':detail,
    'judul':'Staff Detail',
    }
    return render(request,'dashboard/staff/detail_staff.html',context)

def staff_tambah(request):
    form_staff = staff_form(request.POST or None, request.FILES or None)
    if form_staff.is_valid():
        data_staff = form_staff.save(commit=False)
        data_staff.save()
        messages.success(request,'Data staff sudah tersimpan')
    context={
    'form_staff':form_staff,
    'judul':'Tambah Staff'
    }
    return render(request,'dashboard/staff/tambah_staff.html',context)

def staff_edit(request,id=None):
    data_staff = get_object_or_404(staff_model,id=id)
    form_staff = form_staff(request.POST or None, request.FILES or None,instance=data_staff)
    if form_staff.is_valid():
        isi_staff = form_staff.save(commit=False)
        data_staff.save()
        messages.success(request,'Data staff berhasil diedit..')
    context={
    'form_staff':form_staff,
    'judul':'Edit Staff',
    }
    return render(request,'dashboard/staff/tambah_staff.html',context)

def staff_hapus(request,id=None):
    data_staff = get_object_or_404(staff_model,id=id)
    data_staff.delete()
    messages.success(request,'Data staff berhasil dihapus.')
    return redirect('dashboard:staff')
    # return redirect()

def gallery(request):
    data_gallery = gallery_model.objects.all()
    context={
    'gallery':data_gallery,
    'judul':'Gallery'
    }
    return render(request,'dashboard/gallery/list_gallery.html',context)
def gallery_tambah(request):
    form_gallery = gallery_form(request.POST or None, request.FILES or None)
    if form_gallery.is_valid():
        data_gallery = form_gallery.save(commit=False)
        data_gallery.save()
        messages.success(request,'Gallery sudah tersimpan..')
    context={
    'form_gallery':form_gallery,
    'judul':'Tambah Gallery'
    }
    return render(request,'dashboard/gallery/tambah_gallery.html',context)

def gallery_edit(request,id=None):
    data_gallery = get_object_or_404(gallery_model,id=id)
    form_gallery = gallery_form(request.POST or None, request.FILES or None,instance=data_gallery)
    if form_gallery.is_valid():
        isi_gallery = form_gallery.save(commit=False)
        data_gallery.save()
        messages.success(request,'Gallery berhasil diedit..')
    context={
    'form_gallery':form_gallery,
    'judul':'Edit Gallery',
    }
    return render(request,'dashboard/gallery/tambah_gallery.html',context)

def gallery_hapus(request,id=None):
    data_gallery = get_object_or_404(gallery_model,id=id)
    data_gallery.delete()
    messages.success('Gallery berhasil dihapus')
    return redirect('dashboard:gallery')

def berita_tambah(request):
    form_berita=berita_form(request.POST or None, request.FILES or None)
    if form_berita.is_valid():
        data_berita=form_berita.save(commit=False)
        data_berita.save()
        messages.success(request,'Berita berhasil tersimpan..')
    context={
    'form_berita':form_berita,
    'judul':'Buat Berita',
    }
    return render(request,'dashboard/berita/buat_berita.html',context)

def berita_edit(request,slug=None):
    data_berita = get_object_or_404(berita_model,slug=slug)
    form_berita=berita_form(request.POST or None,request.FILES or None,instance=data_berita)
    if form_berita.is_valid():
        isi_berita = form_berita.save(commit=False)
        isi_berita.save()
        messages.success(request,'Berita berhasil diedit')
    context={
    'form_berita':form_berita,
    'judul':'Edit Berita',
    }
    return render(request,'dashboard/berita/buat_berita.html',context)

def berita_hapus(request,slug=None):
    data_berita = get_object_or_404(berita_model,slug=slug)
    data_berita.delete()
    messages.success(request,'Berita berhasil dihapus')
    # return redirect

def berita_detail(request,slug=None):
    data_berita=get_object_or_404(berita_model,slug=slug)
    isi={
    'obj':data_berita,
    'judul':'Detail Berita',
    }
    return render(request,'dashboard/detail_berita.html',isi)

def list_berita(request):
    berita = berita_model.objects.filter(tag='berita')
    context={
    'berita':berita,
    'judul':'list berita'
    }
    return render(request,'dashboard/berita/berita.html',context)

def list_pengumuman(request):
    pengumuman = berita_model.objects.filter(tag='pengumuman')
    context={
    'pengumuman':pengumuman,
    'judul':'list pengumuman',
    }
    return render(request,'dashboard/berita/pengumuman.html',context)






