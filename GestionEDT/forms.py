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

class UCModelForm(forms.ModelForm):
   class Meta:
      model = UC 
      fields = ['CodeMatiere','ECTS','Type']
      labels = {'DateDebut': ('Date du début du semestre: '),
            'NumSemestre': ('Numéro du semestre'),
            'NbSemaines': ('Nombre de semaines de ce semestre')
            }

class SalleModelForm(forms.ModelForm):
   class Meta:
      model = Salle
      fields = ['Nom','Code','Batiment','Capacite','NbPC','Projecteur','Tableaux']
      labels = {'Nom': ('Nom de la salle: '),
            'Code': ('Code de la salle'),
            'Batiment': ('Batiment: '), 'Capacite':('Capacite:'),
            'NbPC': ('Nombre de PC dans la salle'), 'Projecteur':('Présence dun projecteur?'),
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
      fields = ['idGroupe','Libelle','Niveau']
      labels = {'idGroupe': ('Numéro du groupe: '),
            'Libelle': ('Intitulé de ce groupe: '),
            'Niveau': ('Niveau universitaire de ce groupe: ')
            }

class FormationModelForm(forms.ModelForm):
   class Meta:
      model = Formation
      fields = ['idFormation','NomFormation','UFRRattachement']
      labels = {'idFormation': ('Numéro de la formation: '),
            'NomFormation': ('Nom de la formation: '),
            'UFRRattachement': ('UFR de la formation: '),
            }




