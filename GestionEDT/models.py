from django.db import models 
from django.urls import reverse

from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey, EmailField
#import psycopg2.extension

Level_uni = (('L1', ('L1')),('L2', ('L2')),('L3', ('L3')),('M1', ('M1')),('M2', ('M2')))
Semestre_uni = (('S1', ('S1')),('S2', ('S2')),('S3', ('S3')),('S4', ('S4')),
('S5', ('S5')),('S6', ('S6')),('S7', ('S7')),('S8', ('S8')),('S9', ('S9')),('S10', ('S10')))
Statut_prof_uni = (('Professeur des universités', ('Professeur des universités')),
('Maître de conférences', ('Maître de conférences')))

# Create your models here.
class Professeur(models.Model):
  NumProfesseur  = models.IntegerField(primary_key=True)
  Prenom         = models.CharField(max_length=30)       
  Nom            = models.CharField(max_length=30)  
  Adressemail    = models.EmailField(max_length=60)
  Naiss          = models.DateField()
  Statut         = models.CharField(max_length=30, choices=Statut_prof_uni)
  Experience     = models.IntegerField()
  def __str__(self):
    return self.Prenom + ' ' + self.Nom
  def get_absolute_url(self):
     return reverse("professeur-detail", kwargs={"NumProfesseur": self.NumProfesseur})

class Etudiant(models.Model):
   NumEtudiant = models.IntegerField(primary_key=True)
   Prenom      = models.CharField(max_length=30)       
   Nom         = models.CharField(max_length=30)  
   Adressemail = models.EmailField(max_length=60)
   Naiss       = models.DateField()
   Niveau   = models.CharField(max_length=2, choices=Level_uni,default=None) 
   fk_Groupe   = models.ForeignKey("Groupe",on_delete=models.CASCADE)
   def __str__(self):
    return self.Prenom + ' ' + self.Nom
   def get_absolute_url(self):
     return reverse("etudiant-detail", kwargs={"NumEtudiant": self.NumEtudiant})

class UC(models.Model): 
   idUC         = models.IntegerField(primary_key=True)
   NomMatiere   = models.CharField(max_length=30,default=' ')
   ECTS         = models.IntegerField()
   Type         = models.CharField(max_length=15)
   Semestre     = models.CharField(max_length=3, choices=Semestre_uni)
   fk_Formation = models.ForeignKey("Formation",on_delete=models.CASCADE)
   def __str__(self):
    return self.NomMatiere
   def get_absolute_url(self):
     return reverse("uc-detail", kwargs={"idUC": self.idUC})

class Salle(models.Model):
  idSalle   = models.IntegerField(primary_key=True)
  Code      = models.CharField(max_length=100)
  Batiment  = models.CharField(max_length=100)
  Capacite  = models.IntegerField()
  NbPC      = models.IntegerField()
  Projecteur= models.IntegerField()
  Tableaux  = models.IntegerField()
  def __str__(self):
    return self.Code + self.Batiment
  def get_absolute_url(self):
     return reverse('salle-detail', kwargs={"idSalle": self.idSalle})

class Groupe(models.Model):
  idGroupe = models.IntegerField(primary_key=True)
  Libelle  = models.CharField(max_length=100)    
  Niveau   = models.CharField(max_length=2, choices=Level_uni) 
  def __str__(self):
    return self.Libelle
  def get_absolute_url(self):
    return reverse("groupe-detail", kwargs={"idGroupe": self.idGroupe})

class Seance(models.Model): 
  idSeance      = models.IntegerField(primary_key=True)
  TimecodeDebut = models.DateTimeField()
  TimecodeFin   = models.DateTimeField()
  fk_Professeur = models.ForeignKey(Professeur,on_delete=models.CASCADE)
  fk_Groupe     = models.ForeignKey(Groupe,on_delete=models.CASCADE)
  fk_UC         = models.ForeignKey(UC, on_delete=models.CASCADE,default=None)
  fk_Salle      = models.ForeignKey(Salle,on_delete=models.CASCADE)
  def get_absolute_url(self):
    return reverse("seance-detail", kwargs={"idSeance": self.idSeance})

class Formation(models.Model): 
  idFormation     = models.IntegerField(primary_key=True)
  NomFormation    = models.CharField(max_length=100)
  UFRRattachement = models.CharField(max_length=100,default='SEGMI') 
  def __str__(self):
        return self.NomFormation
  def get_absolute_url(self):
     return reverse("formation-detail", kwargs={"idFormation": self.idFormation})

