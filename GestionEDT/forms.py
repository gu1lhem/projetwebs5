from django import forms

from .models import *


class EtudiantModelForm(forms.ModelForm):
   class Meta:
      model = Etudiant
      fields = ['num_etudiant','prenom','nom','adresse_courriel','date_naissance', 'niveau', 'fk_groupe']
      labels = {'prenom': ("Prénom de l'étudiant"), 'nom': ("Nom de l'étudiant"),
            'adresse_courriel': ("Adresse mail de l'étudiant "), 'date_naissance': ("Date de naissance"),
            'niveau' : ("Niveau de l'étudiant"), 'fk_groupe': ("Groupe d'étudiants") 
            }

class UCModelForm(forms.ModelForm):
   class Meta:
      model = UC 
      fields = ['nom_matiere','ects','type_uc','semestre','fk_formation']
      labels = {'nom_matiere': ('Nom de la matière'),
            'ects': ('Coefficient de la matière '),'type_uc': ('Domaine de la matière'),
            'semestre': ('A quel semestre se déroule cette matière?'),
            'fk_formation': ('Dans quel formation?')
            }

class SalleModelForm(forms.ModelForm):
   class Meta:
      model = Salle
      fields = ['id_salle','code','batiment','capacite','nb_pc','projecteur','tableaux'] #! Tableaux a été oublié
      labels = {'code': ('Code de la salle'),
            'batiment': ('Batiment '), 'capacite':('Capacite '),
            'nb_pc': ('Nombre de PC dans la salle'), 'projecteur':("Présence d'un projecteur?"),
            }

class SeanceModelForm(forms.ModelForm):
   class Meta:
      model = Seance
      fields = ['id_seance','timecode_debut','timecode_fin','fk_professeur','fk_groupe','fk_uc','fk_salle']
      labels = {'timecode_debut': ('Date et heure du début du cours'),
            'timecode_fin': ('Date et heure de fin du cours'),
            'fk_profeseur': ('Professeur responsable du cours'),
            'fk_groupe': ("Groupe d'étudiants assistant au cours"),
            'fk_uc': ('Cours'),
            'fk_salle': ('Salle du cours')
            }

class GroupeModelForm(forms.ModelForm):
   class Meta:
      model = Groupe
      fields = ['libelle','niveau']
      labels = {'libelle': ('Intitulé de ce groupe '),
            'niveau': ('Niveau universitaire de ce groupe ')
            }

class FormationModelForm(forms.ModelForm):
   class Meta:
      model = Formation
      fields = ['nom_formation','ufr_rattachement']
      labels = {'nom_formation': ('Nom de la formation'),
            'ufr_rattachement': ('UFR de la formation '),
            }




