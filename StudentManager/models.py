from django.db import models 

from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey, EmailField
#import psycopg2.extension


# Create your models here.
class Individu(models.Model):
   Prenom   = models.CharField(max_length=30)         
   Nom      = models.CharField(max_length=30)  
   Adressemail = models.EmailField(max_length=60)
   Naiss    = models.DateField(auto_now_add=True)
   class Meta:
      abstract = True



class Administratif(Individu):
   Statut = models.CharField(max_length=30)


class Professeur(Individu):
   Statut = models.CharField(max_length=30)
   Experience = models.IntegerField()

class Etudiant(Individu):
   NumEtudiant = models.IntegerField(primary_key=True)

class Personnel(Individu):
   Statut = models.CharField(max_length=30)

class UniteEnseignement(models.Model):
   NomMatière  = models.CharField(max_length=30)
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

class Seance(models.Model):
   IdSeance       = models.IntegerField(primary_key=True)
   TimecodeDebut  = models.DateTimeField(auto_now_add=True)
   TimecodeFIN    = models.DateTimeField(auto_now_add=True)
   fk_UE          = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE)
   fk_Salle       = models.ForeignKey(Salle,on_delete=models.CASCADE)

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
   UFRRattachement = models.CharField(max_length=100,default='Segmi')

class Semestre(models.Model):
   NumSemestre = models.IntegerField(primary_key=True)
   DateDebut   = models.DateTimeField(auto_now_add=True)
   NbSemaines  = models.IntegerField()
   fk_Formation = models.ForeignKey(Formation,on_delete=models.CASCADE) 