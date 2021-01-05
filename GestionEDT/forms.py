from django import forms

from .models import *


class ProfesseurModelForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = ['NumProfesseur','Prenom','Nom','Adressemail','Naiss','Statut','Experience']

class EtudiantModelForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['NumEtudiant','Prenom','Nom','Adressemail','Naiss','fk_Groupe']

class UEModelForm(forms.ModelForm):
    class Meta:
        model = UniteEnseignement 
        fields = ['CodeMatiere','ECTS','Type']

class SalleModelForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['Nom','Code','Batiment','Capacite','NbPC','Projecteur','Tableaux']

class SeanceModelForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['idSeance','TimecodeDebut','TimecodeFIN','fk_Professeur','fk_Etudiant','fk_UE','fk_Salle']

class GroupeModelForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['idGroupe','Libelle','idniveau']

class FormationModelForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['idFormation','NomFormation','UFRRattachement','fk_Semestre']

class SemestreModelForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = ['NumSemestre','DateDebut','NbSemaines']




