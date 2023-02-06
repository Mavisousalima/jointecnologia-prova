from django import forms
from django.forms import TextInput, DateInput

from .models import Alvo

"""class AlvoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=255)
    latitude = forms.DecimalField(label='Latitude')
    longitude = forms.DecimalField(label='Longitude')
    data_expiracao = forms.DateField()"""

class AlvoForm(forms.ModelForm):

    class Meta:
        model = Alvo
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'latitude': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Latitude'
                }),
            'longitude': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Longitude'
                }),
            'data_expiracao': DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Data de expiração'
                }),
        }