from django.forms import ModelForm
from django import forms
from .models import *

class FormTempat(ModelForm):
    class Meta:
        model = Tempat
        fields = '__all__'

        widgets = {
            'koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'Koordinat', 'required':'required'}),
            'provinsi' : forms.TextInput({'class':'form-control', 'placeholder':'Provinsi', 'required':'required'}),
            'daya' : forms.TextInput({'class':'form-control', 'placeholder':'Daya Terkandung', 'required':'required'}),    
            'usaha_id' : forms.Select({'class':'form-control', 'placeholder':'Jenis Usaha', 'required':'required'}),
        }


class FormVideo(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class':'form-control', 'placeholder':'Judul', 'required':'required'}),
            'gambar' : forms.FileInput({'class':'form-control', 'placeholder':'Gambar', 'required':'required'}),
            'publikasi' : forms.DateInput({'type':'date','class':'form-control', 'placeholder':'Publikasi', 'required':'required'}),
            'link' : forms.TextInput({'class':'form-control', 'placeholder':'Link', 'required':'required'}),
            'sumber' : forms.TextInput({'class':'form-control', 'placeholder':'Sumber', 'required':'required'}),
            'jenis_id' : forms.Select({'class':'form-control', 'placeholder':'Jenis Berita', 'required':'required'}),
        }
        
