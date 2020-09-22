from django import forms
from orders.models import order
from django.forms import ModelForm
from django.contrib.auth.models import User

class bukti_Pembayaran(forms.Form):
    buktiPembayaran = forms.FileField(required=True, label='')
