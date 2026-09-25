from django import forms
from .models import ProyectoModels


class ProyectoForms(forms.ModelForm):

    class Meta:
        model = ProyectoModels
        fields = '__all__'

        widgets = {
            'fecha_inicio': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'fecha_termino': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }