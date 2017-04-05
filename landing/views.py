from django.shortcuts import render

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

def ukm(request):
    return render(request,"ukm/ukm.html")

def alumni(request):
    return render(request,"alumni/alumni.html")

def dashboard(request):
    return render(request,"admin/index.html")
