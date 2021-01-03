from django import forms

from .models import *


class SalleModelForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['Nom','Code','Batiment','Capacite','NbPC','Projecteur','Tableaux']

class SemestreModelForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = ['NumSemestre','DateDebut','NbSemaines','fk_Formation']

class FormationModelForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['idFormation','NomFormation','UFRRattachement']


class GroupeModelForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['idgroupe','Libelle','idniveau']

class SeanceModelForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['IdSeance','TimecodeDebut','TimecodeFIN','fk_UE','fk_Salle']