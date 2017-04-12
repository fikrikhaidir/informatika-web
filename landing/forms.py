from django import forms
from .models import alumni_model
from captcha.fields import CaptchaField
from django.core.validators import MaxValueValidator


class alumni_form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = alumni_model    
        fields = "__all__"
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
            'tempat_kerja':{
                'required': "Anda harus mengisi tempat pekerjaan anda"
            },
            'jabatan': {
                'required': 'Anda harus mengisi posisi jabatan anda'
            },
            'tahun_masuk': {
                'required': 'Anda harus mengisi tahun masuk kuliah anda'
            },
            
            }
        widgets = {
            'nama': forms.TextInput(attrs={'placeholder': 'Masukkan nama lengkap anda'}),
            'nim': forms.TextInput(attrs={'placeholder': 'Masukkan NIM (Nomor Induk Mahasiswa) anda tanpa spasi'}),
            'konsentrasi': forms.TextInput(attrs={'placeholder': 'Masukkan konsentrasi anda'}),
            'tempat_kerja': forms.TextInput(attrs={'placeholder': 'Masukkan nama tempat pekerjaan anda'}),
            'jabatan': forms.TextInput(attrs={'placeholder': 'Masukkan jabatan posisi pekerjaan anda'}),
            'tahun_masuk': forms.TextInput(attrs={'placeholder': 'Masukkan tahun masuk anda'}),
            'tahun_keluar': forms.TextInput(attrs={'placeholder': 'Masukkan tahun keluar anda'}),
            
        }

    
        