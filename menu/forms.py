from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class FormCari(forms.Form):
    cari = forms.CharField()

class FormBeli(forms.Form):
    Jumlah = forms.IntegerField()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email', 'password','first_name','last_name', 'email')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('Provinsi', 'Kota',
                  'Kecamatan', 'Kelurahan','alamat', 'profile_pic')
        labels = {
            "alamat": "Alamat",
        }
