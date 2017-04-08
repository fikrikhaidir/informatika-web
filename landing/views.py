from django.shortcuts import render

def home(request):

    return render(request,"home.html")

def galeri(request):
    judul="GALERI INFORMATIKA"
    subJudul= "Galeri Kegiatan Informatika UMS"
    context={
        'judul':judul,
        'subJudul':subJudul,
    }
    return render(request,"berita/galeri.html",context)

def kurikulum(request):
    judul="KURIKULUM INFORMATIKA"
    subJudul= "Kurikulum Program Studi Informatika"
    context={
        'judul':judul,
        'subJudul':subJudul,
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
    judul = "STAFF PENGAJAR"
    subJudul= ""
    context={
        'judul':judul,
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
    return render(request,"ukm/fosti.html")

def himatif(request):
    return render(request,"ukm/himatif.html")

def alumni(request):
    judul = "MANAJEMEN ALUMNI"
    subJudul= "Alumni ? Daftar Disini"
    context={
        'judul':judul,
        'subJudul':subJudul,
    }
    return render(request,"alumni/alumni.html",context)

def dashboard(request):

    return render(request,"admin/index.html")
