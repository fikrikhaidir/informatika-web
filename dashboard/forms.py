from django import forms
from .models import berita_model,staff_model,gallery_model,kurikulum_model
from django.contrib.auth.models import User


class berita_form(forms.ModelForm):
    pilihan = (
        ('Berita','Berita'),
        ('Pengumuman','Pengumuman'),)
    tag = forms.ChoiceField(choices=pilihan)
    class Meta:
        model = berita_model
        fields = [
            'judul',
            'image',
            'content',
            'draft',
            'publish',
            'tag',
            
        ]
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
            'nama_display': forms.TextInput(attrs={'placeholder': 'Masukkan nama yang akan ditampilkan maksimal 14 huruf'}),
            
            'nidn': forms.TextInput(attrs={'placeholder': 'Masukkan NIDN anda tanpa spasi'}),
            'jabatan': forms.TextInput(attrs={'placeholder': 'Masukkan jabatan akademik anda'}),
            'gelar1': forms.TextInput(attrs={'placeholder': 'Masukkan gelar akademik anda S1 sesuai ijazah (ex:S.Kom)'}),
            'gelar2': forms.TextInput(attrs={'placeholder': 'Masukkan gelar akademik anda S2 sesuai ijazah (ex:M.Kom)'}),
            'gelar3': forms.TextInput(attrs={'placeholder': 'Masukkan gelar akademik anda S3 sesuai ijazah (ex:Ph.D)'}),
            'pendidikan1': forms.TextInput(attrs={'placeholder': 'Masukkan jenjang pendidikan/Lulusan S1'}),
            'pendidikan2': forms.TextInput(attrs={'placeholder': 'Masukkan jenjang pendidikan/Lulusan S2(Boleh kosong)'}),
            'pendidikan3': forms.TextInput(attrs={'placeholder': 'Masukkan jenjang pendidikan/Lulusan S3(Boleh kosong)'}),
            'bidang_keahlian1': forms.TextInput(attrs={'placeholder': 'Masukkan lulusan almamater dan bidang keahlian anda S1'}),
            'bidang_keahlian2': forms.TextInput(attrs={'placeholder': 'Masukkan lulusan almamater dan bidang keahlian anda S2(Boleh kosong)'}),
            'bidang_keahlian3': forms.TextInput(attrs={'placeholder': 'Masukkan lulusan almamater dan bidang keahlian anda S3(Boleh kosong)'}),
            'biografi': forms.TextInput(attrs={'placeholder': 'Masukkan biografi singkat(Boleh Kosong)'}),
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
		widgets={
		'judul': forms.TextInput(attrs={'placeholder': 'Masukkan judul foto'}),
		'caption': forms.TextInput(attrs={'placeholder': 'Masukkan keterangan/caption foto'}),
		}

class kurikulum_form(forms.ModelForm):
	class Meta:
		model=kurikulum_model
		fields="__all__"
		widgets={
		'semester': forms.TextInput(attrs={'placeholder': 'Masukkan Semester(ex:3)'}),
		'makul': forms.TextInput(attrs={'placeholder': 'Masukkan nama mata kuliah'}),
		'kode': forms.TextInput(attrs={'placeholder': 'Masukkan kode mata kuliah'}),
		'sks': forms.TextInput(attrs={'placeholder': 'Masukkan sks mata kuliah (ex:3)'}),
		}