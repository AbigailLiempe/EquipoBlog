from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Empleados.models import Avatar

class LiderFormulario(forms.Form):
      nombre = forms.CharField( max_length=50)
      apellido = forms.CharField( max_length=50)
      email = forms.EmailField()
      paginaWeb = forms.CharField( max_length=350)
      descripcion = forms.CharField(widget=forms.Textarea)
      team  = forms.IntegerField()
      
      
class FormColaborador(forms.Form):
      nombre = forms.CharField( max_length=50)
      apellido = forms.CharField( max_length=50)
      email = forms.EmailField()
      paginaWeb = forms.CharField( max_length=350)
      descripcion = forms.CharField(widget=forms.Textarea)
      team  = forms.IntegerField()      
      
class EquipoFormulario(forms.Form):
      
    nombre = forms.CharField( max_length=50)
    team = forms.IntegerField()      

class AvatarFormulario(forms.ModelForm):
      
    class Meta:

      model = Avatar
      fields = ['user', 'imagen']
        
        
class RegistroFormulario(UserCreationForm):
      
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

      model = User
      fields = ['username', 'email', 'password1', 'password2']     