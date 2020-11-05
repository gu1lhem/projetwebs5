from django.db.models import Model, CharField, IntegerField, DateField, DecimalField

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
