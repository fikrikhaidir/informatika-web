from django.shortcuts import render

def home(request):

    return render(request,"home.html")

def kurikulum(request):
    return render(request,"kurikulum/kurikulum.html")

def profil(request):
    return render(request,"profil/profil.html")

def ukm(request):
    return render(request,"ukm/ukm.html")

def alumni(request):
    return render(request,"alumni/alumni.html")

def dashboard(request):
    return render(request,"admin/index.html")
