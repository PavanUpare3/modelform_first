from django import forms 
from .models import Stureg


class StuForm(forms.ModelForm):
    class Meta:
        model = Stureg
        fields = ['name', 'surname', 'password']
       
        