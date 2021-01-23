import io
import csv
from .models import (
    Etudiant
)


def traitement_fichier(donnees):
    cpt = 0
    total = 0
    donnees = io.StringIO(donnees)
    next(donnees)  # si premiere ligne pour les informations

    attributs = ('num_etudiant', 'prenom', 'nom', 'adresse_courriel', 'date_naissance', 'niveau','fk_groupe')
    
    for ligne in csv.reader(donnees, delimiter=','):
            etudiant.save()
    return 

