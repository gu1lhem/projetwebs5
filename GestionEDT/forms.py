from django import forms
from .models import (
    Etudiant,
    Professeur,
    UC,
    Salle,
    Groupe,
    Seance,
    Formation
)

class Form_import_fichier(forms.Form):
    fichier = forms.FileField()