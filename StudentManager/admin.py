from django.contrib import admin

from .models import Individu, Administratif, Professeur, Etudiant,Personel, UniteEnseignement,Salle,Seance,Groupe,Presence,Formation,Semestre

admin.site.register(Individu)
admin.site.register(Administratif)
admin.site.register(Professeur)
admin.site.register(Etudiant)
admin.site.register(Personel)
admin.site.register(UniteEnseignement)
admin.site.register(Salle)
admin.site.register(Seance)
admin.site.register(Groupe)
admin.site.register(Presence)
admin.site.register(Formation)
admin.site.register(Semestre)