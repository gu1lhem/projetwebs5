from django.forms import Forms, CharField, IntegerField, EmailField, DateTimeField

class ajouterEtudiants(Forms):
   prenom         = CharField(label="Prénom", required=True, max_length=30)
   nom            = CharField(label="Nom", required=True, max_length=30)
   num_etudiant   = IntegerField(label="Numéro étudiant", max_length=8)
   courriel       = EmailField(label="Adresse de courriel", max_length=60) # EmailField ajoute contrôle de données https://www.geeksforgeeks.org/emailfield-django-forms/
   date_naissance = DateTimeField()

class ajouterFonctionnaire(Forms):
   prenom         = CharField(label="Prénom", required=True, max_length=30)
   nom            = CharField(label="Nom", required=True, max_length=30)
   status         = CharField(label="Status", required=True, max_length=30)
   courriel       = EmailField(label="Adresse de courriel", max_length=60)
   date_naissance = DateTimeField()
