from django import forms

from .models import *


class ProfesseurModelForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = ['NumProfesseur','Prenom','Nom','Adressemail','Naiss','Statut','Experience']

class EtudiantModelForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['NumEtudiant','Prenom','Nom','Adressemail','Naiss']

class UEModelForm(forms.ModelForm):
    class Meta:
        model = UniteEnseignement 
        fields = ['NomMatiere','ECTS','Type']

class SalleModelForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['Nom','Code','Batiment','Capacite','NbPC','Projecteur','Tableaux']

class SeanceModelForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['idSeance','TimecodeDebut','TimecodeFIN','fk_UE','fk_Salle']

class GroupeModelForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['idGroupe','Libelle','idniveau']

class FormationModelForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['idFormation','NomFormation','UFRRattachement']

class SemestreModelForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = ['NumSemestre','DateDebut','NbSemaines','fk_Formation']




