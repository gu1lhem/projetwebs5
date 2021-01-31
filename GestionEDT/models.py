from django.db import models
from django.urls import reverse
from schedule.models import *

from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey, EmailField
#import psycopg2.extension
from bsct.models import BSCTModelMixin

level_uni = (('L1', ('L1')), ('L2', ('L2')),
             ('L3', ('L3')), ('M1', ('M1')), ('M2', ('M2')))
semestre_uni = (('S1', ('S1')), ('S2', ('S2')), ('S3', ('S3')), ('S4', ('S4')),
                ('S5', ('S5')), ('S6', ('S6')), ('S7', ('S7')), ('S8', ('S8')), ('S9', ('S9')), ('S10', ('S10')))
statut_prof_uni = (('Professeur des universités', ('Professeur des universités')),
                   ('Maître de conférences', ('Maître de conférences')))


# Create your models here.
class Professeur(BSCTModelMixin, models.Model):
    # Classe de Professeur.
    # BSCTModelMixin permet de ne pas écrire les méthodes get_absolute_url, get_delete_url...
    # Doc :
    # * https://pypi.org/project/django-bootstrap-crud-templates/
    # Exemple :
    # * https://github.com/Alem/django-bootstrap-crud-templates/blob/master/demo/crud/models.py

    # attribut entre "" est le verbose name qui nous servira au moment des affichages

    num_professeur = models.AutoField("Numéro du professeur", primary_key=True)
    prenom = models.CharField("Prénom du professeur", max_length=30)
    nom = models.CharField("Nom du professeur", max_length=30)
    adresse_courriel = models.EmailField("Son adresse courriel", max_length=60)
    date_naissance = models.DateField("Sa date de naissance")
    statut = models.CharField(
        "Son statut au sein de la fac", max_length=30, choices=statut_prof_uni)
    experience = models.IntegerField("Ses années d'expériences")

    # La redéfinition de __str__ permet de changer le titre de la page détail
    def __str__(self):
        return self.prenom + ' ' + self.nom

    # Précise le nom à donner à la table - permet les majuscules donc plus jojo
    class Meta:
        verbose_name = "Professeur"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['prenom', 'nom', 'adresse_courriel', 'date_naissance', 'statut', 'experience']


class Etudiant(BSCTModelMixin, models.Model):
    num_etudiant = models.AutoField("Numéro de l'étudiant", primary_key=True)
    prenom = models.CharField("Prénom de l'étudiant", max_length=30)
    nom = models.CharField("Nom de l'étudiant", max_length=30)
    adresse_courriel = models.EmailField("Son adresse courriel", max_length=60)
    date_naissance = models.DateField("Sa date naissance")
    niveau = models.CharField(
        "Son niveau universitaire", max_length=2, choices=level_uni, default=None)
    fk_groupe = models.ForeignKey(
        "Groupe", verbose_name="Groupe", on_delete=models.CASCADE)

    def __str__(self):
        return self.prenom + ' ' + self.nom

    class Meta:
        verbose_name = "Etudiant"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['prenom', 'nom', 'adresse_courriel', 'date_naissance', 'niveau', 'fk_groupe']


class UC(BSCTModelMixin, models.Model):
    id_uc = models.AutoField("Identifiant de l'UC", primary_key=True)
    nom_matiere = models.CharField(
        "Nom de la matière", max_length=30, default=' ')
    ects = models.IntegerField("Son coefficient")
    type_uc = models.CharField("Domaine de l'UC", max_length=15)
    semestre = models.CharField(
        "A quelle semestre appartient-il?", max_length=3, choices=semestre_uni)
    fk_formation = models.ForeignKey(
        "Formation", verbose_name="Formation", on_delete=models.CASCADE)  # clés multiples

    def __str__(self):
        return self.nom_matiere

    class Meta:
        verbose_name = "UC"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['nom_matiere', 'ects', 'type_uc', 'semestre', 'fk_formation']


'''déploiement rapide
class UE(BSCTModelMixin, models.Model):
    id_ue = models.AutoField("Identifiant de l'UE", primary_key=True)
    nom_ue = models.CharField("Nom de la matière", max_length=30, default=' ')
    semestre = models.CharField(
        "A quelle semestre appartient-il?", max_length=3, choices=semestre_uni)
    fk_formation = models.ForeignKey(
        "Formation", verbose_name="Formation", on_delete=models.CASCADE)  # clés multiples

    def __str__(self):
        return self.nom_ue

    class Meta:
        verbose_name = "UE"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['nom_ue', 'fk_formation']
'''


class Salle(BSCTModelMixin, models.Model):
    id_salle = models.AutoField("Identifiant de la salle", primary_key=True)
    code = models.CharField("Nom de la salle", max_length=100)
    batiment = models.CharField("Dans quel bâtiment?", max_length=100)
    capacite = models.IntegerField("Sa capacité")
    nb_pc = models.IntegerField("Le nombre de PCs dans la salle")
    projecteur = models.IntegerField("Le nombre de projecteurs")
    tableaux = models.IntegerField("Le nombre de tableaux?")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Salle"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['code', 'batiment', 'capacite', 'nb_pc', 'projecteur', 'tableaux']


class Groupe(BSCTModelMixin, models.Model):
    id_groupe = models.AutoField("Identifiant du groupe", primary_key=True)
    libelle = models.CharField("Nom du groupe", max_length=100)
    niveau = models.CharField(
        "Niveau du groupe", max_length=2, choices=level_uni)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name = "Groupe"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['libelle', 'niveau']


class Seance(BSCTModelMixin, models.Model):
    id_seance = models.AutoField("Identifiant de la séance", primary_key=True)
    timecode_debut = models.DateTimeField(
        "Date et heure de début de la séance")
    timecode_fin = models.DateTimeField("Date et heure de fin de la séance")
    fk_professeur = models.ForeignKey(
        Professeur, verbose_name="Professeur en charge de la séance", on_delete=models.CASCADE)
    fk_groupe = models.ForeignKey(
        Groupe, verbose_name="Groupe assistant à la séance", on_delete=models.CASCADE)
    fk_uc = models.ForeignKey(
        UC, verbose_name="Matière de la séance", on_delete=models.CASCADE, default=None)
    fk_salle = models.ForeignKey(
        Salle, verbose_name="Dans quelle salle se déroule-t-elle?", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_seance)

    class Meta:
        verbose_name = "Séance"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['timecode_debut', 'timecode_fin', 'fk_professeur', 'fk_groupe', 'fk_uc', 'fk_salle']


class Formation(BSCTModelMixin, models.Model):
    id_formation = models.AutoField(
        "Identifiant de la formation", primary_key=True)
    nom_formation = models.CharField("Nom de la formation", max_length=100)
    ufr_rattachement = models.CharField(
        "UFR de rattachement", max_length=100, default='SEGMI')

    def __str__(self):
        return self.nom_formation

    class Meta:
        verbose_name = "Formation"

    # Fields qui seront récupérés par BSCT pour générer les fields.
    @classmethod
    def get_allowed_fields(cls):
        return ['nom_formation', 'ufr_rattachement']
