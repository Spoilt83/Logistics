from django import forms
from .models import Package


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['client', 'transportist', 'weight', 'dimensions', 'origin', 'destination', 'status']
        labels = {
            'client': 'Cliente',
            'transportist': 'Transportista',
            'weight': 'Peso',
            'dimensions': 'Dimensiones',
            'origin': 'Origen',
            'destination': 'Destino',
            'status': 'Estado'
        }
      