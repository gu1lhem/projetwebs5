from django import forms

from .models import *


class ProfesseurModelForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = ['NumProfesseur','Prenom','Nom','Adressemail','Naiss','Statut','Experience']
        labels = {'DateDebut': ('Date du début du semestre: '),
                'NumSemestre': ('Numéro du semestre'),
                'NbSemaines': ('Nombre de semaines de ce semestre')
                }

class EtudiantModelForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['NumEtudiant','Prenom','Nom','Adressemail','Naiss','fk_Groupe']
        labels = {'DateDebut': ('Date du début du semestre: '),
                'NumSemestre': ('Numéro du semestre'),
                'NbSemaines': ('Nombre de semaines de ce semestre')
                }

class UEModelForm(forms.ModelForm):
    class Meta:
        model = UniteEnseignement 
        fields = ['CodeMatiere','ECTS','Type']
        labels = {'DateDebut': ('Date du début du semestre: '),
                'NumSemestre': ('Numéro du semestre'),
                'NbSemaines': ('Nombre de semaines de ce semestre')
                }

class SalleModelForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['Nom','Code','Batiment','Capacite','NbPC','Projecteur','Tableaux']
        labels = {'DateDebut': ('Date du début du semestre: '),
                'NumSemestre': ('Numéro du semestre'),
                'NbSemaines': ('Nombre de semaines de ce semestre')
                }

class SeanceModelForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['idSeance','TimecodeDebut','TimecodeFIN','fk_Professeur','fk_Etudiant','fk_UE','fk_Salle']
        labels = {'DateDebut': ('Date du début du semestre: '),
                'NumSemestre': ('Numéro du semestre'),
                'NbSemaines': ('Nombre de semaines de ce semestre')
                }

class GroupeModelForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['idGroupe','Libelle','idniveau']
        labels = {'idGroupe': ('Numéro du groupe: '),
                'Libelle': ('Intitulé de ce groupe: '),
                'idniveau': ('Niveau de ce groupe: ')
                }

class FormationModelForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['idFormation','NomFormation','UFRRattachement','fk_Semestre']
        labels = {'idFormation': ('Numéro de la formation: '),
                'NomFormation': ('Nom de la formation: '),
                'UFRRattachement': ('UFR de la formation: '),
                'fk_Semestre': ('Semestre de la formation: ')
                }

class SemestreModelForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = ['NumSemestre','DateDebut','NbSemaines']
        labels = {'DateDebut': ('Date du début du semestre: '),
                'NumSemestre': ('Numéro du semestre: '),
                'NbSemaines': ('Nombre de semaines de ce semestre: ')
                }




