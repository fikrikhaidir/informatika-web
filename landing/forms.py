from django import forms
from .models import berita_model, alumni_model
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class berita_form(forms.ModelForm):
    tag_pilihan = (
        ('Berita','Berita'),
        ('Pengumuman','Pengumuman'),
        )
    tag = forms.ChoiceField(choices=tag_pilihan)
    class Meta:
        model = berita_model
        fields = [
            'judul',
            'image',
            'content',
            'draft',
            'publish',
            
        ]
        label = {
            'judul' : 'Judul Berita/Pengumuman',
            'image' : 'Gambar',
            'publish' : 'Tanggal di publish',
            'draft' : 'Simpan ke konsep',
            'content' : 'Isi Konten',
        }
        error_messages = {
            'judul':{
                'required':'Anda harus mengisi judul berita atau pengumuman'
            },
            'publish':{
                'required':'Anda memastikan tanggal di publish'
            },
            'content':{
                'required':'Isi konten harus diisi'
            },


        }



class alumni_form(forms.ModelForm):
    # captcha = CaptchaField()

    class Meta:
        model = alumni_model    
        fields = ('nama','nim','konsentrasi','pekerjaan','jabatan')
        error_messages = {
            'nama': {
                'required': 'Anda harus mengisi nama lengkap anda'
            },
            'nim' : {
                'required': "Anda harus mengisi NIM anda"
            },
            'konsentrasi' : {
                'required': "Anda harus mengisi konsentrasi anda"
            },
            'pekerjaan':{
                'required': "Anda harus mengisi jenis pekerjaan anda"
            },
            'jabatan': {
                'required': 'Anda harus mengisi posisi jabatan anda'
            },
            
            }
        label = {
            'nama' : 'Nama Lengkap',
            'nim' : 'NIM',
            'konsentrasi' : 'Konsentrasi',
            'pekerjaan' : 'Pekerjaan',
            'jabatan' : 'Jabatan',
        }
        widgets = {
            'nama': forms.TextInput(attrs={'placeholder': 'Masukkan nama lengkap anda'}),
            'nim': forms.TextInput(attrs={'placeholder': 'Masukkan NIM (Nomor Induk Mahasiswa) anda tanpa spasi'}),
            'konsentrasi': forms.TextInput(attrs={'placeholder': 'Masukkan konsentrasi anda'}),
            'pekerjaan': forms.TextInput(attrs={'placeholder': 'Masukkan nama pekerjaan anda'}),
            'jabatan': forms.TextInput(attrs={'placeholder': 'Masukkan jabatan posisi pekerjaan anda'}),
            
        }

    
        