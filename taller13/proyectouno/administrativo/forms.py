from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
        class Meta:
                model = Edificio
                fields = ['nombre', 'direccion', 'ciudad', 'tipo']
                labels = {
                'nombre': _('Ingrese el nombre por favor'),
                'direccion': _('Ingrese la direccion por favor'),
                'ciudad': _('Ingrese la ciudad por favor'),
                'tipo': _('Seleccione el tipo por favor'),
                }

        # El nombre de la ciudad no puede iniciar con la letra mayúscula **L**
        def clean_ciudad(self):
            valor = self.cleaned_data['ciudad']

            if valor[0] == "L":
                raise forms.ValidationError("El nombre de la ciudad no puede empezar con la letra 'L'")
            return valor

class DepartamentoForm(ModelForm):
        class Meta:
                model = Departamento
                fields = ['nombPropietario', 'costoDept', 'cuartos', 'edificio']
                labels = {
                'nombPropietario': _('Ingrese el nombre del propietario por favor'),
                'costoDept': _('Ingrese el costo del departamento por favor'),
                'cuartos': _('Ingrese la cantidad de cuartos que existen por favor'),
                'edificio': _('Seleccione un edificio por favor'),
                }

        # Costo de un departamento no puede ser mayor a $100 mil
        def clean_costoDept(self):
            valor = self.cleaned_data['costoDept']

            if valor > 100000:
                raise forms.ValidationError("El costo del departamento no puede ser mayor a $100 mil")
            return valor

        # Número de cuartos no puede ser 0, ni mayor a 7
        def clean_cuartos(self):
            valor = self.cleaned_data['cuartos']

            if ((valor == 0) or (valor > 7)):
                raise forms.ValidationError("El número de cuartos no puede ser 0, ni mayor a 7")
            return valor

        # El nombre completo de un propietario **no** debe tener menos de 3 palabras.
        def clean_nombPropietario(self):
            valor = self.cleaned_data['nombPropietario']
            validarPropietario = len(valor.split())

            if validarPropietario < 3:
                raise forms.ValidationError("El nombre completo de un propietario no debe tener menos de 3 palabras")
            return valor

class DepartamentoEdificioForm(ModelForm):
        def __init__(self, edificio, *args, **kwargs):
            super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
            self.initial['edificio'] = edificio
            self.fields["edificio"].widget = forms.widgets.HiddenInput()
            print(edificio)

        class Meta:
                model = Departamento
                fields = ['nombPropietario', 'costoDept', 'cuartos', 'edificio']
                labels = {
                'nombPropietario': _('Ingrese el nombre del propietario por favor'),
                'costoDept': _('Ingrese el costo del departamento por favor'),
                'cuartos': _('Ingrese la cantidad de cuartos que existen por favor'),
                'edificio': _('Seleccione un edificio por favor'),
                }

        # Costo de un departamento no puede ser mayor a $100 mil
        def clean_costoDept(self):
            valor = self.cleaned_data['costoDept']

            if valor > 100000:
                raise forms.ValidationError("El costo del departamento no puede ser mayor a $100 mil")
            return valor

        # Número de cuartos no puede ser 0, ni mayor a 7
        def clean_cuartos(self):
            valor = self.cleaned_data['cuartos']

            if ((valor == 0) or (valor > 7)):
                raise forms.ValidationError("El número de cuartos no puede ser 0, ni mayor a 7")
            return valor

        # El nombre completo de un propietario **no** debe tener menos de 3 palabras.
        def clean_nombPropietario(self):
            valor = self.cleaned_data['nombPropietario']
            validarPropietario = len(valor.split())

            if validarPropietario < 3:
                raise forms.ValidationError("El nombre completo de un propietario no debe tener menos de 3 palabras")
            return valor
