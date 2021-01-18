from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *
from .forms import *

import datetime

def home(request):
   # Le contexte title permet, avec un if dans le template, de spécifier un titre à la page.
   # Si aucun titre n'est spécifié, c'est le titre par défaut 'StudentManager' qui est utilisé.
   return render(request, 'home.html', {'title': 'Bienvenue'})


class ProfesseurCreate(CreateView):
   model = Professeur
   template_name = 'professeurs/professeur_create.html'
   form_class = ProfesseurModelForm
   queryset = Professeur.objects.all() # <blog>/<modelname>_list.html
   success_url = '/professeur'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class ProfesseurList(ListView):
   template_name = 'bsct/plain/form.html'
   #queryset = Professeur.objects.all()
   model = Professeur
   def get_context_data(self, **kwargs):
      """ redéfinir la méthode get_context_data pour préciser un layout autre que 'base.html'. """
      context = super(ProfesseurList, self).get_context_data(**kwargs)
      context['bsct_base'] = 'layout.html'
      return context

class ProfesseurDetail(DetailView):
   template_name = 'professeurs/professeur_detail.html'
   queryset = Professeur.objects.all()

   def get_object(self):
      num_professeur = self.kwargs.get("num_professeur")
      return get_object_or_404(Professeur, NumProfesseur=num_professeur)
class ProfesseurUpdate(UpdateView):
   template_name = 'professeurs/professeur_update.html'
   def get_object(self):
      num_professeur=self.kwargs.get("num_professeur")   
      return get_object_or_404(Professeur, NumProfesseur=num_professeur)

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form) 

class ProfesseurDelete(DeleteView):
   template_name = 'professeurs/professeur_delete.html'
   def get_object(self):
      num_professeur = self.kwargs.get("num_professeur")
      return get_object_or_404(Professeur, NumProfesseur=num_professeur)
      return reverse('professeur-list')

class EtudiantCreate(CreateView):
   model = Etudiant
   template_name = 'etudiants/etudiant_create.html'
   form_class = EtudiantModelForm
   queryset = Etudiant.objects.all() # <blog>/<modelname>_list.html
   success_url = '/etudiant'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class EtudiantList(ListView):
   template_name = 'etudiants/etudiant_list.html'
   queryset = Etudiant.objects.all() # <blog>/<modelname>_list.html

class EtudiantDetail(DetailView):
   template_name = 'etudiants/etudiant_detail.html'
   queryset = Etudiant.objects.all()

   def get_object(self):
      id_ = self.kwargs.get("NumEtudiant")
      return get_object_or_404(Etudiant, NumEtudiant=id_)

class EtudiantUpdate(UpdateView):
   template_name = 'etudiants/etudiant_create.html'
   form_class = EtudiantModelForm

   def get_object(self):
      id_ = self.kwargs.get("NumEtudiant")
      return get_object_or_404(Etudiant, NumEtudiant=id_)

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class EtudiantDelete(DeleteView):
   template_name = 'etudiants/etudiant_delete.html'
   
   def get_object(self):
      id_ = self.kwargs.get("NumEtudiant")
      return get_object_or_404(Etudiant, NumEtudiant=id_)
      return reverse('etudiant-list')

class UCCreate(CreateView):
   model = UC
   template_name = 'UCs/uc_create.html'
   form_class = UCModelForm
   queryset = UC.objects.all() # <blog>/<modelname>_list.html
   success_url = '/UC'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class UCList(ListView):
   template_name = 'UCs/uc_list.html'
   queryset = UC.objects.all() # <blog>/<modelname>_list.html

class UCDetail(DetailView):
   template_name = 'UCs/uc_detail.html'
   queryset = UC.objects.all()

   def get_object(self):
      id_ = self.kwargs.get("idUC")
      return get_object_or_404(UC, idUC=id_)

class UCUpdate(UpdateView):
   template_name = 'UCs/uc_create.html'
   form_class = UCModelForm

   def get_object(self):
      id_ = self.kwargs.get("idUC")
      return get_object_or_404(UC, idUC=id_)

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class UCDelete(DeleteView):
   template_name = 'UCs/uc_delete.html'
   
   def get_object(self):
      id_ = self.kwargs.get("idUC")
      return get_object_or_404(UC, idUC=id_)
      return reverse('uc-list')

class SalleCreate(CreateView):
   model = Salle
   template_name = 'salles/salle_create.html'
   form_class = SalleModelForm
   queryset = Salle.objects.all() # <blog>/<modelname>_list.html
   success_url = '/salle'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class SalleList(ListView):
   template_name = 'salles/salle_list.html'
   queryset = Salle.objects.all() # <blog>/<modelname>_list.html

class SalleDetail(DetailView):
   template_name = 'salles/salle_detail.html'
   queryset = Salle.objects.all()

   def get_object(self):
      id_ = self.kwargs.get("idSalle")
      return get_object_or_404(Salle, idSalle=id_)

class SalleUpdate(UpdateView):
   template_name = 'salles/salle_create.html'
   form_class = SalleModelForm

   def get_object(self):
      id_ = self.kwargs.get("idSalle")
      return get_object_or_404(Salle, idSalle=id_)

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class SalleDelete(DeleteView):
   template_name = 'salles/salle_delete.html'
   
   def get_object(self):
      id_ = self.kwargs.get("idSalle")
      return get_object_or_404(Salle, idSalle=id_)

   def get_success_url(self):
      return reverse('salle-list')

class SeanceCreate(CreateView):
   model = Seance
   template_name = 'seances/seance_create.html'
   form_class = SeanceModelForm
   queryset = Seance.objects.all() # <blog>/<modelname>_list.html
   success_url = '/seance'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class SeanceList(ListView):
   template_name = 'seances/seance_list.html'
   queryset = Seance.objects.all() # <blog>/<modelname>_list.html

class SeanceDetail(DetailView):
   template_name = 'seances/seance_detail.html'
   queryset = Seance.objects.all()

   def get_object(self):
      id_ = self.kwargs.get("IdSeance")
      return get_object_or_404(Seance, IdSeance=id_)

class SeanceUpdate(UpdateView):
   template_name = 'seances/seance_create.html'
   form_class = SeanceModelForm

   def get_object(self):
      id_ = self.kwargs.get("IdSeance")
      return get_object_or_404(Seance, IdSeance=id_)

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)
class SeanceDelete(DeleteView):
   template_name = 'seances/seance_delete.html'
   
   def get_object(self):
      id_ = self.kwargs.get("IdSeance")
      return get_object_or_404(Seance, IdSeance=id_)

   def get_success_url(self):
      return reverse('seance-list')

class GroupeCreate(CreateView):
   model = Groupe
   template_name = 'groupes/groupe_create.html'
   form_class = GroupeModelForm
   queryset = Groupe.objects.all() # <blog>/<modelname>_list.html
   success_url = '/groupe'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class GroupeList(ListView):
   template_name = 'groupes/groupe_list.html'
   queryset = Groupe.objects.all() # <blog>/<modelname>_list.html

class GroupeDetail(DetailView):
   template_name = 'groupes/groupe_detail.html'
   queryset = Groupe.objects.all()

   def get_object(self):
      id_ = self.kwargs.get("idGroupe")
      return get_object_or_404(Formation, idGroupe=id_)

class GroupeUpdate(UpdateView):
   template_name = 'groupes/groupe_create.html'
   form_class = GroupeModelForm

   def get_object(self):
      id_ = self.kwargs.get("idGroupe")
      return get_object_or_404(Formation, idGroupe=id_)

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)
class GroupeDelete(DeleteView):
   template_name = 'groupes/groupe_delete.html'
   
   def get_object(self):
      id_ = self.kwargs.get("idGroupe")
      return get_object_or_404(Groupe, idGroupe=id_)

   def get_success_url(self):
      return reverse('groupe-list')
class FormationCreate(CreateView):
   model = Formation
   template_name = 'formations/formation_create.html'
   form_class = FormationModelForm
   queryset = Formation.objects.all() # <blog>/<modelname>_list.html
   success_url = '/formation'

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)

class FormationList(ListView):
   template_name = 'formations/formation_list.html'
   queryset = Formation.objects.all() # <blog>/<modelname>_list.html

class FormationDetail(DetailView):
   template_name = 'formations/formation_detail.html'
   queryset = Formation.objects.all()

   def get_object(self):
      id_ = self.kwargs.get("idFormation")
      return get_object_or_404(Formation, idFormation=id_)

class FormationUpdate(UpdateView):
   template_name = 'formations/formation_create.html'
   form_class = FormationModelForm

   def get_object(self):
      id_ = self.kwargs.get("idFormation")
      return get_object_or_404(Formation, idFormation=id_)

   def form_valid(self, form):
      print(form.cleaned_data)
      return super().form_valid(form)
class FormationDelete(DeleteView):
   template_name = 'formations/formation_delete.html'
   
   def get_object(self):
      id_ = self.kwargs.get("idFormation")
      return get_object_or_404(Formation, idFormation=id_)

   def get_success_url(self):
      return reverse('formation-list')





