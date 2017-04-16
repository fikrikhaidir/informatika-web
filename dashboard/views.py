from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from landing.models import alumni_model
from .forms import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash,authenticate,login,logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings



'''Keperluan Cetak'''
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape, letter
from reportlab.lib import colors

# Create your views here.

def login_view(request):
    title="Login"
    user = request.user
    if user.is_authenticated():
        return redirect('home:dashboard')
    else:
        form_login = user_login_form(request.POST or  None)
        if form_login.is_valid():
            username = form_login.cleaned_data.get("username")
            password = form_login.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            login(request,user)
            return  HttpResponseRedirect (settings.LOGIN_REDIRECT_URL)
        context = {
            "form_login" : form_login,
            "title" : title,

        }
        return render(request,"login.html",context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required()
def password_ubah(request):
    title = 'Password'
    if request.method == 'POST':
        form_password = ubah_password(request.user, data=request.POST)
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request, form_password.user)
            messages.success(request, "Password sudah terganti.")
            # return redirect("/")
    else:
        form_password =ubah_password(request.user)
    data = {
        'form_password': form_password,
        'title' : title,
    }
    return render(request, "dashboard/akun/ubah_password.html", data)

@login_required()
def alumni_dashboard(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_alumni = alumni_model.objects.all()
    context = {
    'data_alumni':data_alumni,
    'title':'Data Alumni',
    }
    return render(request,"dashboard/halaman/alumni.html",context)

@login_required()
def cetak_rekapan_alumni(request):
    if not request.user.is_staff and not request.user.is_superuser:
        raise Http404
    # pengaturan respon berformat pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rekapan_alumni.pdf"'

    # mengambil daftar kehadiran dan mengubahnya menjadi data ntuk tabel
    data = alumni_model.objects.all()
    table_data = []

    table_data.append([ "NO","Nama","NIM","Konsentrasi","Perusahaan","Posisi","Thn Masuk, Lulus" ])
    i = 1
    for x in data:
        table_data.append([ i,x.nama, x.nim, x.konsentrasi, x.tempat_kerja,x.jabatan,str(x.tahun_masuk)+", "+str(x.tahun_keluar) ])
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
    # logo = "static/img/logo_ums.jpg"
    # im = Image(logo, 2*inch, 2*inch)
    # content.append(im)
    content.append(Paragraph('Daftar Rekapan Mahasiswa Alumni Informatika', styles['Title']))
    content.append(Spacer(1,12))
    # content.append(Paragraph('Berikut ini adalah rekapannya' , styles['Normal']))
    content.append(Spacer(1,12))
    content.append(pendaftar_table)
    content.append(Spacer(1,36))
    # content.append(Paragraph('Mengetahui, ', styles['Normal']))
    # content.append(Spacer(1,48))
    # content.append(Paragraph('Wakil Dekan III ', styles['Normal']))

    # menghasilkan pdf untk di download
    doc.build(content)
    return response

@login_required()
def staff(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_staff = staff_model.objects.all().filter(posisi='staff')
    context={
    'staff':data_staff,
    'judul':'Staff',
    }
    return render(request,'dashboard/staff/list_staff.html',context)

@login_required()
def dosen_tetap(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_staff = staff_model.objects.all().filter(posisi='dosen tetap')
    context={
    'staff':data_staff,
    'judul':'Staff',
    }
    return render(request,'dashboard/staff/list_dosen_tetap.html',context)

@login_required()
def dosen_profesi(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_staff = staff_model.objects.all().filter(posisi='dosen profesi')
    context={
    'staff':data_staff,
    'judul':'Staff',
    }
    return render(request,'dashboard/staff/list_dosen_profesi.html',context)

@login_required()
def staff_tambah(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    form_staff = staff_form(request.POST or None, request.FILES or None)
    if form_staff.is_valid():
        data_staff = form_staff.save(commit=False)
        data_staff.posisi = 'staff'
        data_staff.save()
        # messages.success(request,'Data staff sudah tersimpan')
        return redirect('dashboard:staff')
    context={
    'form_staff':form_staff,
    'judul':'Tambah Staff'
    }
    return render(request,'dashboard/staff/tambah_staff.html',context)

@login_required()
def dosen_tetap_tambah(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    form_staff = staff_form(request.POST or None, request.FILES or None)
    if form_staff.is_valid():
        data_staff = form_staff.save(commit=False)
        data_staff.posisi = 'dosen tetap'
        data_staff.save()
        # messages.success(request,'Data staff sudah tersimpan')
        return HttpResponseRedirect('../')
    context={
    'form_staff':form_staff,
    'judul':'Tambah Staff'
    }
    return render(request,'dashboard/staff/tambah_dosen_tetap.html',context)

@login_required()
def dosen_profesi_tambah(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    form_staff = staff_form(request.POST or None, request.FILES or None)
    if form_staff.is_valid():
        data_staff = form_staff.save(commit=False)
        data_staff.posisi = 'dosen profesi'
        data_staff.save()
        # messages.success(request,'Data staff sudah tersimpan')
        return HttpResponseRedirect('../')
    context={
    'form_staff':form_staff,
    'judul':'Tambah Staff'
    }
    return render(request,'dashboard/staff/tambah_dosen_profesi.html',context)

@login_required()
def staff_edit(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_staff = get_object_or_404(staff_model,id=id)
    form_staff = staff_form(request.POST or None, request.FILES or None,instance=data_staff)
    if form_staff.is_valid():
        isi_staff = form_staff.save(commit=False)
        data_staff.save()
        # messages.success(request,'Data staff berhasil diedit..')
        return redirect('dashboard:staff')
    context={
    'form_staff':form_staff,
    'judul':'Edit Staff',
    }
    return render(request,'dashboard/staff/tambah_staff.html',context)

@login_required()
def dosen_tetap_edit(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_staff = get_object_or_404(staff_model,id=id)
    form_staff = staff_form(request.POST or None, request.FILES or None,instance=data_staff)
    if form_staff.is_valid():
        isi_staff = form_staff.save(commit=False)
        data_staff.save()
        # messages.success(request,'Data staff berhasil diedit..')
        return HttpResponseRedirect('../../')
    context={
    'form_staff':form_staff,
    'judul':'Edit Staff',
    }
    return render(request,'dashboard/staff/tambah_dosen_tetap.html',context)

@login_required()
def dosen_profesi_edit(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_staff = get_object_or_404(staff_model,id=id)
    form_staff = staff_form(request.POST or None, request.FILES or None,instance=data_staff)
    if form_staff.is_valid():
        isi_staff = form_staff.save(commit=False)
        data_staff.save()
        # messages.success(request,'Data staff berhasil diedit..')
        return HttpResponseRedirect('../..')
    context={
    'form_staff':form_staff,
    'judul':'Edit Staff',
    }
    return render(request,'dashboard/staff/tambah_dosen_profesi.html',context)

@login_required()
def staff_hapus(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_staff = get_object_or_404(staff_model,id=id)
    data_staff.delete()
    # messages.success(request,'Data staff berhasil dihapus.')
    return redirect('dashboard:staff')
    # return redirect()

@login_required()
def dosen_tetap_hapus(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_staff = get_object_or_404(staff_model,id=id)
    data_staff.delete()
    # messages.success(request,'Data staff berhasil dihapus.')
    return redirect('dashboard:dosen_tetap')
    # return redirect()

@login_required()
def dosen_profesi_hapus(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_staff = get_object_or_404(staff_model,id=id)
    data_staff.delete()
    # messages.success(request,'Data staff berhasil dihapus.')
    return redirect('dashboard:dosen_profesi')
    # return redirect()

@login_required()
def gallery(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_gallery = gallery_model.objects.all()
    context={
    'gallery':data_gallery,
    'judul':'Gallery'
    }
    return render(request,'dashboard/gallery/list_gallery.html',context)

@login_required()
def gallery_tambah(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    form_gallery = gallery_form(request.POST or None, request.FILES or None)
    if form_gallery.is_valid():
        data_gallery = form_gallery.save(commit=False)
        data_gallery.save()
        # messages.success(request,'Gallery sudah tersimpan..')
        return redirect('dashboard:gallery')
    context={
    'form_gallery':form_gallery,
    'judul':'Tambah Gallery'
    }
    return render(request,'dashboard/gallery/tambah_gallery.html',context)

@login_required()
def gallery_edit(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_gallery = get_object_or_404(gallery_model,id=id)
    form_gallery = gallery_form(request.POST or None, request.FILES or None,instance=data_gallery)
    if form_gallery.is_valid():
        isi_gallery = form_gallery.save(commit=False)
        data_gallery.save()
        # messages.success(request,'Gallery berhasil diedit..')
        return redirect('dashboard:gallery')
    context={
    'form_gallery':form_gallery,
    'judul':'Edit Gallery',
    }
    return render(request,'dashboard/gallery/tambah_gallery.html',context)

@login_required()
def gallery_hapus(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_gallery = get_object_or_404(gallery_model,id=id)
    data_gallery.delete()
    # messages.success('Gallery berhasil dihapus')
    return redirect('dashboard:gallery')

@login_required()
def berita_tambah(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    form_berita=berita_form(request.POST or None, request.FILES or None)
    if form_berita.is_valid():
        data_berita=form_berita.save(commit=False)
        data_berita.tag='Berita'
        data_berita.save()
        # messages.success(request,'Berita berhasil tersimpan..')
        return HttpResponseRedirect('../')
    context={
    'form_berita':form_berita,
    'judul':'Buat Berita',
    }
    return render(request,'dashboard/berita/buat_berita.html',context)

@login_required()
def berita_edit(request,slug=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_berita = get_object_or_404(berita_model,slug=slug)
    form_berita=berita_form(request.POST or None,request.FILES or None,instance=data_berita)
    if form_berita.is_valid():
        isi_berita = form_berita.save(commit=False)
        isi_berita.save()
        # messages.success(request,'Berita berhasil diedit')
        return HttpResponseRedirect('../..')
    context={
    'form_berita':form_berita,
    'judul':'Edit Berita',
    }
    return render(request,'dashboard/berita/buat_berita.html',context)

@login_required()
def berita_hapus(request,slug=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_berita = get_object_or_404(berita_model,slug=slug)
    data_berita.delete()
    # messages.success(request,'Berita berhasil dihapus')
    return redirect('dashboard:berita')

@login_required()
def berita_detail(request,slug=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_berita=get_object_or_404(berita_model,slug=slug)
    isi={
    'obj':data_berita,
    'judul':'Detail Berita',
    }
    return render(request,'dashboard/berita/detail_berita.html',isi)

@login_required()
def list_berita(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    list_berita_list = berita_model.objects.filter(tag='Berita')
    page = request.GET.get('page',1)
    paginator = Paginator(list_berita_list, 10)

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
    context['judul'] = 'Berita'

    return render(request,'dashboard/berita/berita.html',context)

@login_required()
def list_pengumuman(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    list_pengumuman_list = berita_model.objects.filter(tag='Pengumuman')
    page = request.GET.get('page',1)
    paginator = Paginator(list_pengumuman_list, 10)

    try:
        pengumuman = paginator.page(page)
    except PageNotAnInteger:
        pengumuman = paginator.page(1)
    except EmptyPage:
        pengumuman = paginator.page(paginator.num_pages)
    context ={
        'pengumuman' : pengumuman,
    }
    query = request.GET.get("q")
    if query:
        list_pengumuman_list = list_pengumuman_list.filter(
            Q(judul__icontains=query)|
            Q(content__icontains=query)
        ).distinct()
        context['pengumuman'] = list_pengumuman_list
    context['judul'] = 'Pengumuman'
    return render(request,'dashboard/berita/pengumuman.html',context)

@login_required()
def pengumuman_tambah(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    form_berita=berita_form(request.POST or None, request.FILES or None)
    if form_berita.is_valid():
        data_berita=form_berita.save(commit=False)
        data_berita.tag = 'Pengumuman'
        data_berita.save()
        # messages.success(request,'Pengumuman berhasil tersimpan..')
        return HttpResponseRedirect('../')
    context={
    'form_berita':form_berita,
    'judul':'Buat Berita',
    }
    return render(request,'dashboard/berita/buat_berita.html',context)

@login_required()
def pengumuman_edit(request,slug=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_berita = get_object_or_404(berita_model,slug=slug)
    form_berita=berita_form(request.POST or None,request.FILES or None,instance=data_berita)
    if form_berita.is_valid():
        isi_berita = form_berita.save(commit=False)
        isi_berita.save()
        # messages.success(request,'Pengumuman berhasil diedit')
        return HttpResponseRedirect('../..')
    context={
    'form_berita':form_berita,
    'judul':'Edit Berita',
    }
    return render(request,'dashboard/berita/buat_berita.html',context)

@login_required()
def pengumuman_hapus(request,slug=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_berita = get_object_or_404(berita_model,slug=slug)
    data_berita.delete()
    # messages.success(request,'Berita berhasil dihapus')
    return redirect('dashboard:pengumuman')

@login_required()
def kurikulum(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    kurikulum = kurikulum_model.objects.all()
    context={
    'kurikulum':kurikulum,
    'judul':'Kurikulum',
    }
    return render(request,'dashboard/halaman/kurikulum/list_kurikulum.html',context)

@login_required()
def ukm(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data = ukm_model.objects.all()
    context={
    'ukm':data,

    }
    return render(request,'dashboard/halaman/ukm.html',context)


@login_required()
def kurikulum_tambah(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    form_kurikulum = kurikulum_form(request.POST or None)
    if form_kurikulum.is_valid():
        data_kurikulum = form_kurikulum.save(commit=False)
        data_kurikulum.save()
        return redirect('dashboard:kurikulum')
    context={
    'form_kurikulum':form_kurikulum,
    'judul':'Form Kurikulum',
    }
    return render(request,'dashboard/halaman/kurikulum/buat_kurikulum.html',context)

@login_required()
def kurikulum_edit(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_edit = get_object_or_404(kurikulum_model,id=id)
    form_kurikulum = kurikulum_form(request.POST or None, request.FILES or None,instance=data_edit)
    if form_kurikulum.is_valid():
        isi_kurikulum = form_kurikulum.save(commit=False)
        data_edit.save()
        # messages.success(request,'Gallery berhasil diedit..')
        return redirect('dashboard:kurikulum')
    context={
    'form_kurikulum':form_kurikulum,
    'judul':'Edit Kurikulum',
    }
    return render(request,'dashboard/halaman/kurikulum/buat_kurikulum.html',context)

@login_required()
def kurikulum_hapus(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data_kurikulum = get_object_or_404(kurikulum_model,id=id)
    data_kurikulum.delete()
    # messages.success(request,'Berita berhasil dihapus')
    return redirect('dashboard:kurikulum')

@login_required()
def dokumen(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    dokumen = dokumen_model.objects.all()
    context={
    'dokumen':dokumen,
    'judul':'Dokumen',
    }
    return render(request,'dashboard/umum/umum.html',context)

@login_required()
def dokumen_tambah(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    form_dokumen = dokumen_form(request.POST or None, request.FILES or None)
    if form_dokumen.is_valid():
        data = form_dokumen.save(commit=False)
        data.save()
        return HttpResponseRedirect("../")
    context={
    'form_dokumen':form_dokumen,
    'judul':'Form Dokumen',
    }
    return render(request,'dashboard/umum/buat_dokumen.html',context)

@login_required()
def dokumen_edit(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data = get_object_or_404(dokumen_model,id=id)
    form_dokumen = dokumen_form(request.POST or None, request.FILES or None,instance=data)
    if form_dokumen.is_valid():
        dok = form_dokumen.save(commit=False)
        dok.save()
        return HttpResponseRedirect('../..')
    context={
    'form_dokumen' : form_dokumen,
    'judul':'Form Dokumen',
    }
    return render(request,'dashboard/umum/buat_dokumen.html',context)

@login_required()
def dokumen_detail(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data = get_object_or_404(dokumen_model,id=id)
    context={
    'obj':data,
    'judul':'Dokumen',
    }
    return render(request,'dashboard/umum/umum.html',context)

@login_required()
def dokumen_hapus(request,id=None):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    data = get_object_or_404(dokumen_model,id=id)
    data.delete()
    return redirect('dashboard:dokumen')

@login_required()
def ukm_tambah(request):
    if not request.user.is_active and not request.user.is_authenticated:
        raise Http404
    form_ukm = ukm_form(request.POST or None, request.FILES or None)
    if form_ukm.is_valid():
        data_ukm = form_ukm.save(commit=False)
        data_ukm.save()
        return redirect('dashboard:ukm')
    context={
    'form_ukm':form_ukm,
    'judul':'Form UKM',
    }
    return render(request,'dashboard/halaman/buat_ukm.html',context)

@login_required()
def ukm_edit(request,id=None):
    data_isi = get_object_or_404(ukm_model,id=id)
    form_ukm = ukm_form(request.POST or None, request.FILES or None,instance=data_isi)
    if form_ukm.is_valid():
        data = form_ukm.save(commit=False)
        data.save()
        return redirect('dashboard:ukm')
    context={
    'form_ukm':form_ukm,
    'judul':'Edit UKM',
    }
    return render(request,'dashboard/halaman/buat_ukm.html',context)

@login_required()
def ukm_hapus(request,id=None):
    data_ukm = get_object_or_404(ukm_model,id=id)
    data_ukm.delete()
    return redirect('dashboard:ukm')

