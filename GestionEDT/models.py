from django.db import models 
from django.urls import reverse

from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey, EmailField
#import psycopg2.extension

Level_uni = ((1, ('L1')),(2, ('L2')),(3, ('L3')),(4, ('M1')),(5, ('M2')),)
Semestre_uni = ((1, ('S1')),(2, ('S2')),(3, ('S3')),(4, ('S4')),(5, ('S5')),(6, ('S6')))

# Create your models here.
class Professeur(models.Model):
  NumProfesseur  = models.IntegerField(primary_key=True)
  Prenom         = models.CharField(max_length=30)       
  Nom            = models.CharField(max_length=30)  
  Adressemail    = models.EmailField(max_length=60)
  Naiss          = models.DateField()
  Statut         = models.CharField(max_length=30)
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
   Semestre     = models.CharField(max_length=2, choices=Semestre_uni)
   fk_Formation = models.ForeignKey("Formation",on_delete=models.CASCADE) # clés multiples
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

class Seance(models.Model): 
  idSeance      = models.IntegerField(primary_key=True)
  TimecodeDebut = models.DateTimeField()
  TimecodeFin   = models.DateTimeField()
  fk_Professeur = models.ForeignKey(Professeur,on_delete=models.CASCADE)
  fk_Groupe     = models.ForeignKey(Etudiant,on_delete=models.CASCADE)
  fk_UC         = models.ForeignKey(UC, on_delete=models.CASCADE,default=None)
  fk_Salle      = models.ForeignKey(Salle,on_delete=models.CASCADE)
  def get_absolute_url(self):
    return reverse("seance-detail", kwargs={"idSeance": self.idSeance})

class Groupe(models.Model):
  idGroupe = models.IntegerField(primary_key=True)
  Libelle  = models.CharField(max_length=100)    
  Niveau   = models.CharField(max_length=2, choices=Level_uni) 
  def __str__(self):
    return self.Libelle
  def get_absolute_url(self):
    return reverse("groupe-detail", kwargs={"idGroupe": self.idGroupe})
   
class Formation(models.Model): 
  idFormation     = models.IntegerField(primary_key=True)
  NomFormation    = models.CharField(max_length=100)
  UFRRattachement = models.CharField(max_length=100,default='SEGMI') 
  def __str__(self):
        return self.NomFormation
  def get_absolute_url(self):
     return reverse("formation-detail", kwargs={"idFormation": self.idFormation})

