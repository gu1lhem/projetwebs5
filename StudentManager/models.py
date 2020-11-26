from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey

#import psycopg2.extension


# Create your models here.
class Individu(Model):
   Prenom      = CharField(max_length=30)       
   Nom         = CharField(max_length=30)  
   Adressemail = CharField(max_length=50)
   Naiss       = DateField(auto_now_add=True)
   class Meta:
      abstract = True



class Administratif(Individu):
   Statut      = CharField(max_length=30)


class Professeur(Individu):
   Statut      = CharField(max_length=30)
   Experience  = IntegerField()

class Etudiant(Individu):
   idEtudiant  = IntegerField(primary_key=True)

class Personnel(Individu):
   Statut      = CharField(max_length=30)



class UniteEnseignement(Model):
   NomMatiere  = CharField(max_length=30)
   ECTS        = IntegerField()
   Type        = CharField(max_length=15)

class Seance(Model):
   IdSeance    = IntegerField(primary_key=True)
   TimecodeDebut = DateTimeField(auto_now_add=True)
   TimecodeFIN = DateTimeField(auto_now_add=True)
   fk_UE       = ForeignKey(UniteEnseignement, on_delete=CASCADE)

class Groupe(Model):
   idgroupe    = IntegerField(primary_key=True)
   Libelle     = CharField(max_length=100)    
   idniveau    = CharField(max_length=6)
   
class Presence(Model):
   boolPresence = BooleanField(default=False)
   fk_Etudiant = ForeignKey(Etudiant, on_delete=CASCADE)
   fk_Seance   = ForeignKey(Seance, on_delete=CASCADE)


class Salle(Model):
   Nom         = IntegerField(primary_key=True)
   Code        = CharField(max_length=100)
   Batiment    = CharField(max_length=100)
   Capacite    = IntegerField()
   NbPC        = IntegerField()
   Projecteur  = IntegerField()
   Tableaux    = IntegerField()

class Semestre(Model):
   DateDebut   = DateTimeField(auto_now_add=True)
   NbSemaines  = IntegerField()

class Formation(Model):
   NomFormation = CharField(max_length=100)
   UFRRattachement = CharField(max_length=100,default='SEGMI')





""" %%% """"""" Code du prof """""" %%%" """

class Si_Personnel(Model):
   """
   """
   prenom       = CharField(max_length=30)
   nom         = CharField(max_length=30)
   courriel      = CharField(max_length=50, blank=True, null=True)
   num_siham     = IntegerField(unique=True)
   d_creation    = DateField(blank=True, null=True)
   d_modification = DateField(blank=True, null=True)
   cnu         = IntegerField()
   miage        = IntegerField()
   fid_statut    = IntegerField()

   def __str__(self):
     return self.prenom + "." + self.nom + ', Statut='+ str(self.fid_statut)

class Si_Statut(Model):
   """
   """
   libelle      = CharField(max_length=20)
   nb_h_min      = IntegerField()
   nb_h_max      = IntegerField(blank=True, null=True)

   def __str__(self):
     return self.libelle+'/ id ='+str(self.id)

class Si_Ec(Model):
   """
   """
   id_liaison    = IntegerField()
   credit       = DecimalField(max_digits=3, decimal_places=1)
   d_creation    = DateField()
   libelle      = CharField(max_length=100)
   h_cm         = IntegerField()
   h_td         = IntegerField()
   h_tp         = IntegerField(blank=True, null=True)
   h_stage      = IntegerField(blank=True, null=True)
   lmd         = IntegerField(blank=True, null=True)

   def __str__(self):
     return self.libelle+'/ id ='+str(self.id)   


class Si_View_Ls(Model):
   """
   """
   prenom       = CharField(max_length=20)
   nom         = CharField(max_length=20)
   fid_pers      = IntegerField()
   libelle_ec    = CharField(max_length=100)
   fid_ec       = IntegerField(blank=True, null=True)
   groupe       = CharField(max_length=25)
   sem         = CharField(max_length=2)
   h_cm         = DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
   h_td         = DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
   hetd         = DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)

   def __str__(self):
     return 'LIGNE : '+ self.id +' :' + self.nom + "." + self.prenom + "." + self.ec + "." + self.groupe
