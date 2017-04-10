from django import forms
from .models import berita_model,staff_model,gallery_model
from django.contrib.auth.models import User


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
class staff_form(forms.ModelForm):
	class Meta:
		model = staff_model
		fields = '__all__'
		label = {
		'nama' : 'Nama Lengkap',
		'nidn' : 'NIDN',
		'jabatan' : 'Jabatan Akademik',
		'gelar' : 'Gelar Akademik',
		'pendidikan1' : 'Jenjang S1',
		'pendidikan2' : 'Jenjang S2',
		'pendidikan3' : 'Jenjang S3',
		'bidang_keahlian1': 'Bidang Keahlian dari Lulusan S1',
		'bidang_keahlian2': 'Bidang Keahlian dari Lulusan S2',
		'bidang_keahlian3': 'Bidang Keahlian dari Lulusan S3',
		}
		error_messages = {
		'nama':{
		'required':'Anda harus mengisi nama lengkap anda'
		},
		'nidn':{
		'required':'Anda harus mengisi NIDN anda'
		},
		'jabatan':{
		'required':'Anda harus mengisi jabatan akademik dosen'
		},
		'gelar':{
		'required':'Anda harus mengisi gelar akademik dosen'
		},
		'pendidikan1':{
		'required':'Anda harus mengisi jenjang pendidikan'
		},
		'bidang_keahlian1':{
		'required':'Anda harus mengisi bidang keahlian dan almamater'
		},
		}
		widgets = {
            'nama': forms.TextInput(attrs={'placeholder': 'Masukkan nama lengkap anda'}),
            'nidn': forms.TextInput(attrs={'placeholder': 'Masukkan NIDN anda tanpa spasi'}),
            'jabatan': forms.TextInput(attrs={'placeholder': 'Masukkan jabatan akademik anda'}),
            'gelar': forms.TextInput(attrs={'placeholder': 'Masukkan gelar akademik anda'}),
            'pendidikan1': forms.TextInput(attrs={'placeholder': 'Masukkan jenjang pendidikan/Lulusan S1'}),
            'pendidikan2': forms.TextInput(attrs={'placeholder': 'Masukkan jenjang pendidikan/Lulusan S2'}),
            'pendidikan3': forms.TextInput(attrs={'placeholder': 'Masukkan jenjang pendidikan/Lulusan S3'}),
            'bidang_keahlian1': forms.TextInput(attrs={'placeholder': 'Masukkan lulusan almamater dan bidang keahlian anda S1'}),
            'bidang_keahlian2': forms.TextInput(attrs={'placeholder': 'Masukkan lulusan almamater dan bidang keahlian anda S2'}),
            'bidang_keahlian3': forms.TextInput(attrs={'placeholder': 'Masukkan lulusan almamater dan bidang keahlian anda S3'}),
        }

class gallery_form(forms.ModelForm):
	class Meta:
		model=gallery_model
		fields="__all__"
		error_messages = {
		'judul':{
		'required':'Anda harus mengisi judul foto'
		},
		'caption':{
		'required':'Anda harus memasukkan caption foto'
		},
		'image':{
		'required':'Anda harus memasukkan foto'
		}
		}
		label={
		'judul':'Judul Foto',
		'caption':'Caption Foto',
		'image':'Foto',
		}
		widgets={
		'judul': forms.TextInput(attrs={'placeholder': 'Masukkan judul foto'}),
		'caption': forms.TextInput(attrs={'placeholder': 'Masukkan keterangan/caption foto'}),
		}