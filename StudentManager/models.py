from django.db.models import Model, CharField, IntegerField, DateField, DecimalField

<<<<<<< HEAD
import psycopg2.extension


# Create your models here.
class Individu(models.Model):
    Prenom = models.CharField(max_length=30)         
    Nom = models.CharField(max_length=30)  
    Adressemail = models.CharField(max_length=50)
    Naiss = models.DateField(auto_now_add=True)
    class Meta:
        abstract = True



class Administratif(Individu):
    Statut = models.CharField(max_length=30)


class Professeur(Individu):
    Statut = models.CharField(max_length=30)
    Experience = models.IntegerField()

class Etudiant(Individu):
    idEtudiant = models.IntegerField(primary_key=True)

class Personnel(Individu):
    Statut = models.CharField(max_length=30)



class UniteEnseignement(models.Model):
    NomMatière = models.CharField(max_length=30)
    ECTS = models.IntegerField()
    Type = models.CharField(max_length=15)

class Seance(models.Model):
    IdSeance = models.IntegerField(primary_key=True)
    TimecodeDebut = models.DateTimeField(auto_now_add=True)
    TimecodeFIN = models.DateTimeField(auto_now_add=True)
    fk_UE = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE)

class Groupe(models.Model):
    idgroupe = models.IntegerField(primary_key=True)
    Libelle = models.CharField(max_length=100)     
    idniveau = models.CharField(max_length=6)
    
class Presence(models.Model):
    boolPresence = models.BooleanField(default=False)
    fk_Etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    fk_Seance = models.ForeignKey(Seance, on_delete=models.CASCADE)


class Salle(models.Model):
    Nom = models.IntegerField(primary_key=True)
    Code = models.CharField(max_length=100)
    Batiment = models.CharField(max_length=100)
    Capacite = models.IntegerField()
    NbPC = models.IntegerField()
    Projecteur = models.IntegerField()
    Tableaux = models.IntegerField()

class Semestre(models.Model):
    DateDebut = models.DateTimeField(auto_now_add=True)
    NbSemaines = models.IntegerField()

class Formation(models.Model):
    NomFormation = models.CharField(max_length=100)
    UFRRattachement = models.CharField(max_length=100,default='Segmi')
=======
class Si_Personnel(Model):
   """
   """
   prenom         = CharField(max_length=30)
   nom            = CharField(max_length=30)
   courriel       = CharField(max_length=50, blank=True, null=True)
   num_siham      = IntegerField(unique=True)
   d_creation     = DateField(blank=True, null=True)
   d_modification = DateField(blank=True, null=True)
   cnu            = IntegerField()
   miage          = IntegerField()
   fid_statut     = IntegerField()

   def __str__(self):
      return self.prenom + "." + self.nom + ', Statut='+ str(self.fid_statut)

class Si_Statut(Model):
   """
   """
   libelle        = CharField(max_length=20)
   nb_h_min       = IntegerField()
   nb_h_max       = IntegerField(blank=True, null=True)

   def __str__(self):
      return self.libelle+'/ id ='+str(self.id)

class Si_Ec(Model):
   """
   """
   id_liaison     = IntegerField()
   credit         = DecimalField(max_digits=3, decimal_places=1)
   d_creation     = DateField()
   libelle        = CharField(max_length=100)
   h_cm           = IntegerField()
   h_td           = IntegerField()
   h_tp           = IntegerField(blank=True, null=True)
   h_stage        = IntegerField(blank=True, null=True)
   lmd            = IntegerField(blank=True, null=True)

   def __str__(self):
      return self.libelle+'/ id ='+str(self.id)   


class Si_View_Ls(Model):
   """
   """
   prenom         = CharField(max_length=20)
   nom            = CharField(max_length=20)
   fid_pers       = IntegerField()
   libelle_ec     = CharField(max_length=100)
   fid_ec         = IntegerField(blank=True, null=True)
   groupe         = CharField(max_length=25)
   sem            = CharField(max_length=2)
   h_cm           = DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
   h_td           = DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
   hetd           = DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)

   def __str__(self):
      return 'LIGNE : '+ self.id +' :' + self.nom + "." + self.prenom + "." + self.ec + "." + self.groupe
>>>>>>> f9e5b4bb8c2ca566f9e6ff58615cef79a0edd7c3
