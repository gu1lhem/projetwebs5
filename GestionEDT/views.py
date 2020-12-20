from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

from GestionEDT.models import Individu, UniteEnseignement, Salle, Seance, Semestre, Groupe, Formation

import datetime

def home(request):
   # Le contexte title permet, avec un if dans le template, de spécifier un titre à la page.
   # Si aucun titre n'est spécifié, c'est le titre par défaut 'StudentManager' qui est utilisé.
   return render(request, 'home.html', {'title': 'Bienvenue'})

class IndividuCreate(CreateView):
    model = Individu
    fields = ['Prenom','Nom','Adressemail','Naiss']

class IndividuUpdate(UpdateView):
    model = Individu
    fields = ['Prenom','Nom','Adressemail','Naiss']

class IndividuDelete(DeleteView):
    model = Individu
    success_url = reverse_lazy('author-list')

class UniteEnseignementCreate(CreateView):
    model = UniteEnseignement
    fields = ['NomMatière','ECTS','Type']

class UniteEnseignementUpdate(UpdateView):
    model = UniteEnseignement
    fields = ['NomMatière','ECTS','Type']

class UniteEnseignementDelete(DeleteView):
    model = UniteEnseignement
    success_url = reverse_lazy('author-list')

class SalleCreate(CreateView):
    model = Salle
    fields = ['Nom','Code','Batiment','Capacite','NbPC','Projecteur','Tableaux']

class SalleUpdate(UpdateView):
    model = Salle
    fields = ['Nom','Code','Batiment','Capacite','NbPC','Projecteur','Tableaux']

class SalleDelete(DeleteView):
    model = Salle
    success_url = reverse_lazy('author-list')

class SeanceCreate(CreateView):
    model = Seance 
    fields = ['IdSeance','TimecodeDebut','TimecodeFIN']

class SeanceCreate(UpdateView):
    model = Seance 
    fields = ['IdSeance','TimecodeDebut','TimecodeFIN']
    
class SeanceDelete(DeleteView):
    model = Seance
    success_url = reverse_lazy('author-list')

class GroupeCreate(CreateView):
    model = Groupe
    fields = ['Libelle']

class GroupeCreate(UpdateView):
    model = Groupe
    fields = ['Libelle']

class GroupeDelete(DeleteView):
    model = Groupe
    success_url = reverse_lazy('author-list')

class FormationCreate(CreateView):
    model = Formation
    fields = ['NomFormation']
    fields = ['UFRRattachement']

class FormationCreate(UpdateView):
    model = Formation
    fields = ['NomFormation']
    fields = ['UFRRattachement']

class FormationDelete(DeleteView):
    model = Formation
    success_url = reverse_lazy('author-list')

class SemestreCreate(CreateView):
    model = Semestre
    fields = ['NumSemestre']
    fields = ['DateDebut']
    fields = ['NbSemaines']

class SemestreCreate(UpdateView):
    model = Semestre
    fields = ['NumSemestre']
    fields = ['DateDebut']
    fields = ['NbSemaines']

class SemestreDelete(DeleteView):
    model = Semestre
    success_url = reverse_lazy('author-list')







