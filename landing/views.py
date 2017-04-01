from django.shortcuts import render

def home(request):

    return render(request,"home.html")

def kurikulum(request):
    return render(request,"kurikulum.html")

def profil(request):
    return render(request,"profil.html")

def ukm(request):
    return render(request,"ukm.html")

def alumni(request):
    return render(request,"alumni.html")
