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
    judul = "MANAJEMEN ALUMNI"
    subJudul= "Alumni ? Daftar Disini"
    context={
        'judul':judul,
        'subJudul':subJudul,
    }
    return render(request,"alumni/alumni.html",context)

def dashboard(request):

    return render(request,"admin/index.html")
