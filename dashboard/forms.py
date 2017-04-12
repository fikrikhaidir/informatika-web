from django import forms
from .models import berita_model,staff_model,gallery_model,kurikulum_model,beranda_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User



User = get_user_model()
class user_login_form(forms.Form):
    username = forms.CharField(error_messages={'required':'Mohon untuk mengisi username'}, widget=forms.TextInput(attrs={'placeholder':'Masukkan username anda.'}))
    password = forms.CharField(error_messages={'required':'Mohon untuk mengisi password'},widget=forms.PasswordInput(attrs={'placeholder':'Masukkan password anda.'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password :
            user = authenticate(username=username,password=password)
            if not user :
                raise forms.ValidationError("Username dan password yang anda masukkan salah.")
            elif not user.check_password(password):
                raise forms.ValidationError("Username dan password yang anda masukkan salah.")
            elif not user.is_active:
                raise forms.ValidationError("Username dan password yang anda masukkan salah.")
        return super(user_login_form, self).clean(*args,**kwargs)

class ubah_password(PasswordChangeForm):
    class Meta :
        model = User
        fields = [
            'old_password',
            'new_password',
            'new_confirmation_password',
        ]


class berita_form(forms.ModelForm):
    class Meta:
        model = berita_model
        fields = [
            'judul',
            'image',
            'content',
            'draft',
            'publish',
            
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
            'penelitian': forms.TextInput(attrs={'placeholder': 'Masukkan link penelitian google scholar dosen'}),
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

class beranda_form(forms.ModelForm):
    judul_besar = forms.CharField(error_messages={'required':'Mohon untuk mengisi judul tagline'}, widget=forms.TextInput(attrs={'placeholder':'Masukkan judul tagline (ex: Sesuaikan dirimu dengan zaman).'}))
    keterangan_singkat = forms.CharField(error_messages={'required':'Mohon untuk mengisi keterangan singkat'},widget=forms.TextInput(attrs={'placeholder':'Masukkan keterangan singkat (ex: Dengan kurikulum yang selalu diperbarui ).'}))
    nama_button = forms.CharField(error_messages={'required':'Mohon untuk mengisi nama button yang akan ditampilkan'},widget=forms.TextInput(attrs={'placeholder':'Masukkan nama button yang akan ditampilkan (ex: Lihat Kurikulum ).'}))
    link_button = forms.CharField(error_messages={'required':'Mohon untuk mengisi link untuk button'},widget=forms.TextInput(attrs={'placeholder':'Masukkan alamat url untuk button (ex: http://informatika.ums.ac.id/kurikulum ).'}))
  
    class Meta:
        model = beranda_model
        fields = "__all__"
