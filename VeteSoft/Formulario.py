from django import forms

from VeteSoft.models import *

class RegistroMedicoForm(forms.ModelForm):

    class Meta:
        model = Medico

        fields =[
            'Documento',
            'Nombres',
            'PrimerApellido',
            'SegundoApellido',
            'FechaNacimiento',
            'Genero',
            'Celular',
            'Direccion'
        ]

        labels={
            'Documento'       : 'Documento',
            'Nombres'         : 'Nombres',
            'PrimerApellido'  : 'PrimerApellido',
            'SegundoApellido' : 'SegundoApellido',
            'FechaNacimiento' : 'FechaNacimiento',
            'Genero'          : 'Genero',
            'Celular'         : 'Celular',
            'Direccion'       : 'Direccion',
        }

        widgets={
            'Documento'       : forms.TextInput(attrs={'class':'form-control','placeholder':'Documento'}),        
            'Nombres'         : forms.TextInput(attrs={'class':'form-control'}), 
            'PrimerApellido'  : forms.TextInput(attrs={'class':'form-control'}), 
            'SegundoApellido' : forms.TextInput(attrs={'class':'form-control'}), 
            'FechaNacimiento' : forms.TextInput(attrs={'class':'form-control','placeholder':'DD/MM/AAA'}),
            'Genero'          : forms.Select(attrs={'class':'form-control'}),
            'Celular'         : forms.TextInput(attrs={'class':'form-control'}), 
            'Direccion'       : forms.TextInput(attrs={'class':'form-control'}), 
        }

class ActualizarMedico(forms.ModelForm):
    class Meta:
        model = Medico

        fields =[
            'Documento',
            'Nombres',
            'PrimerApellido',
            'SegundoApellido',
            'Genero',
            'Celular',
            'Direccion'
        ]

        labels={
            'Documento'       : 'Documento',
            'Nombres'         : 'Nombres',
            'PrimerApellido'  : 'PrimerApellido',
            'SegundoApellido' : 'SegundoApellido',
            'Genero'          : 'Genero',
            'Celular'         : 'Celular',
            'Direccion'       : 'Direccion',
        }

        widgets={
            'Documento'       : forms.TextInput(attrs={'class':'form-control'}),        
            'Nombres'         : forms.TextInput(attrs={'class':'form-control'}), 
            'PrimerApellido'  : forms.TextInput(attrs={'class':'form-control'}), 
            'SegundoApellido' : forms.TextInput(attrs={'class':'form-control'}), 
            'Genero'          : forms.Select(attrs={'class':'form-control'}),
            'Celular'         : forms.TextInput(attrs={'class':'form-control'}), 
            'Direccion'       : forms.TextInput(attrs={'class':'form-control'}), 
        }

class RegistroClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields =[
            'Documento',
            'Nombres',
            'PrimerApellido',
            'SegundoApellido',
            'FechaNacimiento',
            'Genero',
            'Celular',
            'Direccion'
        ]

        labels={
            'Documento'       : 'Documento',
            'Nombres'         : 'Nombres',
            'PrimerApellido'  : 'PrimerApellido',
            'SegundoApellido' : 'SegundoApellido',
            'FechaNacimiento' : 'FechaNacimiento',
            'Genero'          : 'Genero',
            'Celular'         : 'Celular',
            'Direccion'       : 'Direccion',
        }

        widgets={
            'Documento'       : forms.TextInput(attrs={'class':'form-control','placeholder':'Documento'}),        
            'Nombres'         : forms.TextInput(attrs={'class':'form-control'}), 
            'PrimerApellido'  : forms.TextInput(attrs={'class':'form-control'}), 
            'SegundoApellido' : forms.TextInput(attrs={'class':'form-control'}), 
            'FechaNacimiento' : forms.TextInput(attrs={'class':'form-control','placeholder':'DD/MM/AAA'}),
            'Genero'          : forms.Select(attrs={'class':'form-control'}),
            'Celular'         : forms.TextInput(attrs={'class':'form-control'}), 
            'Direccion'       : forms.TextInput(attrs={'class':'form-control'}), 
        }

class ActualizarCliente(forms.ModelForm):
    class Meta:
        model = Cliente

        fields =[
            'Documento',
            'Nombres',
            'PrimerApellido',
            'SegundoApellido',
            'Genero',
            'Celular',
            'Direccion'
        ]

        labels={
            'Documento'       : 'Documento',
            'Nombres'         : 'Nombres',
            'PrimerApellido'  : 'PrimerApellido',
            'SegundoApellido' : 'SegundoApellido',
            'Genero'          : 'Genero',
            'Celular'         : 'Celular',
            'Direccion'       : 'Direccion',
        }

        widgets={
            'Documento'       : forms.TextInput(attrs={'class':'form-control'}),        
            'Nombres'         : forms.TextInput(attrs={'class':'form-control'}), 
            'PrimerApellido'  : forms.TextInput(attrs={'class':'form-control'}), 
            'SegundoApellido' : forms.TextInput(attrs={'class':'form-control'}), 
            'Genero'          : forms.Select(attrs={'class':'form-control'}),
            'Celular'         : forms.TextInput(attrs={'class':'form-control'}), 
            'Direccion'       : forms.TextInput(attrs={'class':'form-control'}), 
        }