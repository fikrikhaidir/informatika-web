from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import berita_model,alumni_model
from .forms import alumni_form,berita_form
from django.contrib import messages
from django.http import HttpResponse

'''Keperluan Cetak'''
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors


def home(request):

    return render(request,"home.html")

def kurikulum(request):
    return render(request,"kurikulum/kurikulum.html")

def profil(request):
    judul="PROFIL INFORMATIKA"
    context={
        'judul':judul,
    }
    return render(request,"profil/profil.html",context)

def identitas(request):
    judul = "TENTANG INFORMATIKA"
    context={
        'judul':judul,
    }
    return render(request,"profil/identitas.html",context)

def staff(request):
    judul = "STAFF PENGAJAR"
    context={
        'judul':judul,
    }
    return render(request,"profil/staff.html",context)

def visi(request):
    judul = "VISI DAN MISI"
    context = {
        'judul':judul,
    }
    return render(request,"profil/visi.html",context)


def ukm(request):
    return render(request,"ukm/ukm.html")

def alumni(request):
    form_alumni = alumni_form(request.POST or None)
    if form_alumni.is_valid():
        isi = form_alumni.save(commit=False)
        isi.save()
        messages.success(request,'Terima Kasih anda telah mengisi data alumni. Data anda sudah tersimpan.')
    context = {
    'form_alumni':form_alumni,
    'title':'Alumni',
    }
    return render(request,'alumni/alumni.html',context)

def alumni_dashboard(request):
    data_alumni = alumni_model.objects.all()
    context = {
    'data_alumni':data_alumni,
    'title':'Data Alumni',
    }
    return render(request,"admin/tables.html",context)

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




def dashboard(request):
    return render(request,"admin/index.html")

'''Berita view'''
# def berita_list(request):
#     list_berita_list = berita.objects.filter(draft=False).filter(tag='Pengumuman').filter(publish__lte=Now())

#     #pagination
#     page = request.GET.get('page',1)
#     paginator = Paginator(list_berita_list, 5)


#     try:
#         beritas = paginator.page(page)
#     except PageNotAnInteger:
#         beritas = paginator.page(1)
#     except EmptyPage:
#         beritas = paginator.page(paginator.num_pages)
#     context ={
#         'beritas' : beritas,
#     }
#     query = request.GET.get("q")
#     if query:
#         list_berita_list = list_berita_list.filter(
#             Q(judul__icontains=query)|
#             Q(content__icontains=query)
#         ).distinct()
#         context['beritas'] = list_berita_list
#     context['title'] = 'Berita'


#     return render(request,"dashboard/dashboard_berita_member.html",context)


