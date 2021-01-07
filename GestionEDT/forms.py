from django import forms

from .models import *


class ProfesseurModelForm(forms.ModelForm):
   class Meta:
      model = Professeur
      fields = ['NumProfesseur','Prenom','Nom','Adressemail','Naiss','Statut','Experience']
      labels = {'NumProfesseur': ("Numéro de professeur "),
            'Prenom': ("Prenom du professeur"), 'Nom': ("Nom du professeur"),
            'Adressemail': ("Adresse mail du professeur "), 'Naiss': ("Date de naissance"),
            'Statut': ("Statut de l'enseignant "), 'Experience': ("Niveau d'expérience du professeur")
            }

class EtudiantModelForm(forms.ModelForm):
   class Meta:
      model = Etudiant
      fields = ['NumEtudiant','Prenom','Nom','Adressemail','Naiss','fk_Groupe']
      labels = {'NumEtudiant': ("Numéro d'étudiant "),
            'Prenom': ("Prenom de l'étudiant"), 'Nom': ("Nom de l'étudiant"),
            'Adressemail': ("Adresse mail de l'étudiant "), 'Naiss': ("Date de naissance"),
            'fk_Groupe': ("Groupe d'étudiants") 
            }

class UCModelForm(forms.ModelForm):
   class Meta:
      model = UC 
      fields = ['idUC','NomMatiere','ECTS','Type','Semestre','fk_Formation']
      labels = {'idUC': ('Numéro de la matière '),'NomMatiere': ('Nom de la matière'),
            'ECTS': ('Coefficient de la matière '),'Type': ('Domaine de la matière'),
            'Semestre': ('A quel semestre se déroule cette matière?'),
            'fk_Formation': ('Dans quel formation?')
            }

class SalleModelForm(forms.ModelForm):
   class Meta:
      model = Salle
      fields = ['idSalle','Code','Batiment','Capacite','NbPC','Projecteur','Tableaux']
      labels = {'idSalle': ('Numéro de la salle'),
            'Code': ('Code de la salle'),
            'Batiment': ('Batiment '), 'Capacite':('Capacite '),
            'NbPC': ('Nombre de PC dans la salle'), 'Projecteur':("Présence d'un projecteur?"),
            }

class SeanceModelForm(forms.ModelForm):
   class Meta:
      model = Seance
      fields = ['idSeance','TimecodeDebut','TimecodeFin','fk_Professeur','fk_Groupe','fk_UC','fk_Salle']
      labels = {'idSeance': ('Numéro de séance '),
            'TimecodeDebut': ('Date et heure du début du cours'),
            'TimecodeFin': ('Date et heure de fin du cours'),
            'fk_UC': ('Cours'),
            'fk_Profeseur': ('Professeur responsable du cours'),
            'fk_Groupe': ("Groupe d'étudiants assistant au cours"),
            'fk_Salle': ('Salle du cours')
            }

class GroupeModelForm(forms.ModelForm):
   class Meta:
      model = Groupe
      fields = ['idGroupe','Libelle','Niveau']
      labels = {'idGroupe': ('Numéro du groupe '),
            'Libelle': ('Intitulé de ce groupe '),
            'Niveau': ('Niveau universitaire de ce groupe ')
            }

class FormationModelForm(forms.ModelForm):
   class Meta:
      model = Formation
      fields = ['idFormation','NomFormation','UFRRattachement']
      labels = {'idFormation': ('Numéro de la formation '),
            'NomFormation': ('Nom de la formation'),
            'UFRRattachement': ('UFR de la formation '),
            }




