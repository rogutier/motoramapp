from django import forms
from .models import Vehiculo


class VehiculoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Vehiculo
        exclude = []
