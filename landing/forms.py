from django import forms
from .models import alumni_model
from captcha.fields import CaptchaField





class alumni_form(forms.ModelForm):
    captcha = CaptchaField()

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

    
        