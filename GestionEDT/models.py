from django.db import models 
from django.urls import reverse

from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey, EmailField
#import psycopg2.extension


# Create your models here.
class Professeur(models.Model):
   NumProfesseur  = models.IntegerField(primary_key=True)
   Prenom         = models.CharField(max_length=30)         
   Nom            = models.CharField(max_length=30)  
   Adressemail    = models.EmailField(max_length=60)
   Naiss          = models.DateField()
   Statut         = models.CharField(max_length=30)
   Experience     = models.IntegerField()
   def get_absolute_url(self):
      return reverse("professeur-detail", kwargs={"NumProfesseur": self.NumProfesseur})

class Etudiant(models.Model):
   NumEtudiant = models.IntegerField(primary_key=True)
   Prenom      = models.CharField(max_length=30)         
   Nom         = models.CharField(max_length=30)  
   Adressemail = models.EmailField(max_length=60)
   Naiss       = models.DateField()
   fk_Groupe   = models.ForeignKey("Groupe",on_delete=models.CASCADE)
   def get_absolute_url(self):
      return reverse("etudiant-detail", kwargs={"NumEtudiant": self.NumEtudiant})

class UniteEnseignement(models.Model): #fk key vers Formation et Semestre
   CodeMatiere   = models.CharField(primary_key=True,max_length=30,default=' ')
   ECTS          = models.IntegerField()
   Type          = models.CharField(max_length=15)
   def get_absolute_url(self):
      return reverse("ue-detail", kwargs={"CodeMatiere": self.CodeMatiere})

class Salle(models.Model):
   Nom         = models.IntegerField(primary_key=True)
   Code        = models.CharField(max_length=100)
   Batiment    = models.CharField(max_length=100)
   Capacite    = models.IntegerField()
   NbPC        = models.IntegerField()
   Projecteur  = models.IntegerField()
   Tableaux    = models.IntegerField()
   def get_absolute_url(self):
      return reverse('salle-detail', kwargs={"Nom": self.Nom})

class Seance(models.Model): # date du cours puis heure début et heure fin?
   idSeance       = models.IntegerField(primary_key=True)
   TimecodeDebut  = models.DateTimeField()
   TimecodeFIN    = models.DateTimeField()
   fk_Professeur  = models.ForeignKey(Professeur,on_delete=models.CASCADE)
   fk_Etudiant    = models.ForeignKey(Etudiant,on_delete=models.CASCADE)
   fk_UE          = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE)
   fk_Salle       = models.ForeignKey(Salle,on_delete=models.CASCADE)
   def get_absolute_url(self):
      return reverse("seance-detail", kwargs={"idSeance": self.idSeance})

class Groupe(models.Model):
   Level_uni = (('L1'),('L2'),('L3'),('M1'),('M2'),)
   idGroupe = models.IntegerField(primary_key=True)
   Libelle  = models.CharField(max_length=100)     
   Niveau = models.CharField(max_length=2,choices=Level_uni) 
   def get_absolute_url(self):
      return reverse("groupe-detail", kwargs={"idGroupe": self.idGroupe})
    
class Formation(models.Model): # pourquoi Semestre comme clés étrangères déjà?
   idFormation = models.IntegerField(primary_key=True)
   NomFormation = models.CharField(max_length=100)
   UFRRattachement = models.CharField(max_length=100,default='SEGMI')
   fk_Semestre = models.ForeignKey("Semestre",on_delete=models.CASCADE) 
   def get_absolute_url(self):
      return reverse("formation-detail", kwargs={"idFormation": self.idFormation})

class Semestre(models.Model):
   NumSemestre = models.IntegerField(primary_key=True)
   DateDebut   = models.DateTimeField()
   NbSemaines  = models.IntegerField()
   def get_absolute_url(self):
      return reverse("semestre-detail", kwargs={"NumSemestre": self.NumSemestre})

