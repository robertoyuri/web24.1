from django.forms import ModelForm
from django import forms
from .models import Paciente, Medico, Consulta

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'nascimento', 'endereco', 'cidade', 'cep', 'cpf', 'rg', 'plano']
        widgets = {'nascimento': forms.TextInput(attrs={'data-mask':'DD/MM/AAAA', 'class':'form-control'}),
                   'nome': forms.TextInput(attrs={'class':'form-control'}),
                   'endereco': forms.TextInput(attrs={'class':'form-control'}),
                   'cidade': forms.TextInput(attrs={'class':'form-control'}),
                   'rg': forms.TextInput(attrs={'class':'form-control'}),
                   'plano': forms.TextInput(attrs={'class':'form-control'}),
                   'cep': forms.TextInput(attrs={'data-mask':'00000-000', 'class':'form-control'}),
                   'cpf': forms.TextInput(attrs={'data-mask':'000.000.000-00', 'class':'form-control'})
                   }


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'nascimento', 'endereco', 'cidade', 'cep', 'cpf', 'rg', 'crm']
        widgets = {'nascimento': forms.TextInput(attrs={'data-mask':'DD/MM/AAAA', 'class':'form-control'}),
                   'nome': forms.TextInput(attrs={'class':'form-control'}),
                   'endereco': forms.TextInput(attrs={'class':'form-control'}),
                   'cidade': forms.TextInput(attrs={'class':'form-control'}),
                   'rg': forms.TextInput(attrs={'class':'form-control'}),
                   'crm': forms.TextInput(attrs={'class':'form-control'}),
                   'cep': forms.TextInput(attrs={'data-mask':'00000-000', 'class':'form-control'}),
                   'cpf': forms.TextInput(attrs={'data-mask':'000.000.000-00', 'class':'form-control'})
                   }

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'hora', 'medico', 'paciente', 'prontuario']
        widgets = {'data': forms.TextInput(attrs={'data-mask':'DD/MM/AAAA', 'class':'form-control', 'id':'validationCustom02'}),
                   'hora': forms.TextInput(attrs={'data-mask':'00:00', 'class':'form-control'}),
                   'medico': forms.Select(attrs={'class':'form-control'}),
                   'paciente': forms.Select(attrs={'class':'form-control form-control-lg'}),
                   'prontuario': forms.Textarea(attrs={'class':'form-control form-control-lg'})
                   }