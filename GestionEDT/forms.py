from django import forms

from .models import *


class ProfesseurModelForm(forms.ModelForm):
   class Meta:
      model = Professeur
      fields = ['num_professeur','prenom','nom','adresse_courriel','date_naissance','statut','experience']
      labels = {'num_professeur': ("Numéro de professeur "),
            'prenom': ("prenom du professeur"), 'nom': ("nom du professeur"),
            'adresse_courriel': ("Adresse mail du professeur "), 'date_naissance': ("Date de naissance"),
            'statut': ("statut de l'enseignant "), 'experience': ("Niveau d'expérience du professeur")
            }

class EtudiantModelForm(forms.ModelForm):
   class Meta:
      model = Etudiant
      fields = ['num_etudiant','prenom','nom','adresse_courriel','date_naissance', 'niveau', 'fk_groupe']
      labels = {'num_etudiant': ("Numéro d'étudiant "),
            'prenom': ("prenom de l'étudiant"), 'nom': ("nom de l'étudiant"),
            'adresse_courriel': ("Adresse mail de l'étudiant "), 'date_naissance': ("Date de naissance"),
            'niveau' : ("niveau de l'étudiant"), 'fk_groupe': ("Groupe d'étudiants") 
            }

class UCModelForm(forms.ModelForm):
   class Meta:
      model = UC 
      fields = ['id_uc','nom_matiere','ects','type_uc','semestre','fk_formation']
      labels = {'id_uc': ('Numéro de la matière '),'nom_matiere': ('nom de la matière'),
            'ects': ('Coefficient de la matière '),'type_uc': ('Domaine de la matière'),
            'semestre': ('A quel semestre se déroule cette matière?'),
            'fk_formation': ('Dans quel formation?')
            }

class SalleModelForm(forms.ModelForm):
   class Meta:
      model = Salle
      fields = ['id_salle','code','batiment','capacite','nb_pc','projecteur','tableaux'] #! Tableaux a été oublié
      labels = {'id_salle': ('Numéro de la salle'),
            'code': ('Code de la salle'),
            'batiment': ('Batiment '), 'capacite':('Capacite '),
            'nb_pc': ('nombre de PC dans la salle'), 'projecteur':("Présence d'un projecteur?"),
            }

class SeanceModelForm(forms.ModelForm):
   class Meta:
      model = Seance
      fields = ['id_seance','timecode_debut','timecode_fin','fk_professeur','fk_groupe','fk_uc','fk_salle']
      labels = {'id_seance': ('Numéro de séance '),
            'timecode_debut': ('Date et heure du début du cours'),
            'timecode_fin': ('Date et heure de fin du cours'),
            'fk_profeseur': ('Professeur responsable du cours'),
            'fk_groupe': ("Groupe d'étudiants assistant au cours"),
            'fk_uc': ('Cours'),
            'fk_salle': ('Salle du cours')
            }

class GroupeModelForm(forms.ModelForm):
   class Meta:
      model = Groupe
      fields = ['id_groupe','libelle','niveau']
      labels = {'id_groupe': ('Numéro du groupe '),
            'libelle': ('Intitulé de ce groupe '),
            'niveau': ('Niveau universitaire de ce groupe ')
            }

class FormationModelForm(forms.ModelForm):
   class Meta:
      model = Formation
      fields = ['id_formation','nom_formation','ufr_rattachement']
      labels = {'id_formation': ('Numéro de la formation '),
            'nom_formation': ('nom de la formation'),
            'ufr_rattachement': ('UFR de la formation '),
            }




