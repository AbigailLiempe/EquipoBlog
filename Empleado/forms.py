from django import forms

class FormTeamLeader(forms.Form):
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
      
class FormTeam(forms.Form):
      
    nombre = forms.CharField( max_length=50)
    team = forms.IntegerField()      