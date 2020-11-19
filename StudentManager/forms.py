from django import forms

class SelectNom(forms.Form):
   def_nom = forms.CharField(label = 'Nom', required=True, widget=forms.TextInput,max_length=10)

   def clean_def_nom(self):
      data = self.cleaned_data['def_nom']
      return data
