from django.db import models 
from django.urls import reverse

from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey, EmailField
#import psycopg2.extension


# Create your models here.
class Professeur(models.Model):
   NumProfesseur = models.IntegerField(primary_key=True)
   Prenom   = models.CharField(max_length=30)         
   Nom      = models.CharField(max_length=30)  
   Adressemail = models.EmailField(max_length=60)
   Naiss    = models.DateField(auto_now_add=True)
   Statut = models.CharField(max_length=30)
   Experience = models.IntegerField()

class Etudiant(models.Model):
   NumEtudiant = models.IntegerField(primary_key=True)
   Prenom   = models.CharField(max_length=30)         
   Nom      = models.CharField(max_length=30)  
   Adressemail = models.EmailField(max_length=60)
   Naiss    = models.DateField(auto_now_add=True)

class UniteEnseignement(models.Model):
   NomMatiere  = models.CharField(max_length=30,primary_key=True)
   ECTS        = models.IntegerField()
   Type        = models.CharField(max_length=15)

class Salle(models.Model):
   Nom      = models.IntegerField(primary_key=True)
   Code     = models.CharField(max_length=100)
   Batiment = models.CharField(max_length=100)
   Capacite = models.IntegerField()
   NbPC     = models.IntegerField()
   Projecteur  = models.IntegerField()
   Tableaux    = models.IntegerField()
   def get_absolute_url(self):
      return reverse('salle-detail', kwargs={'pk': self.pk})

class Seance(models.Model):
   IdSeance       = models.IntegerField(primary_key=True)
   TimecodeDebut  = models.DateTimeField()
   TimecodeFIN    = models.DateTimeField()
   fk_UE          = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE)
   fk_Salle       = models.ForeignKey(Salle,on_delete=models.CASCADE)
   def get_absolute_url(self):
      return reverse("seance-detail", kwargs={"pk": self.pk})

class Groupe(models.Model):
   idgroupe = models.IntegerField(primary_key=True)
   Libelle  = models.CharField(max_length=100)     
   idniveau = models.CharField(max_length=6)
    
class Presence(models.Model):
   boolPresence   = models.BooleanField(default=False)
   fk_Etudiant    = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
   fk_Seance      = models.ForeignKey(Seance, on_delete=models.CASCADE)

class Formation(models.Model):
   idFormation = models.IntegerField(primary_key=True)
   NomFormation = models.CharField(max_length=100)
   UFRRattachement = models.CharField(max_length=100,default='SEGMI')

class Semestre(models.Model):
   NumSemestre = models.IntegerField(primary_key=True)
   DateDebut   = models.DateTimeField()
   NbSemaines  = models.IntegerField()
   fk_Formation = models.ForeignKey(Formation,on_delete=models.CASCADE) 
