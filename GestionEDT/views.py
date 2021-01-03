from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Individu, UniteEnseignement, Salle, Seance, Semestre, Groupe, Formation
from .forms import SalleModelForm, SemestreModelForm

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
    template_name = 'salles/salle_create.html'
    form_class = SalleModelForm
    queryset = Salle.objects.all() # <blog>/<modelname>_list.html
    success_url = 'salle/'

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
        id_ = self.kwargs.get("Code")
        return get_object_or_404(Salle, id=id_)

class SalleUpdate(UpdateView):
    template_name = 'salles/salle_create.html'
    form_class = SalleModelForm

    def get_object(self):
        id_ = self.kwargs.get("Code")
        return get_object_or_404(Salle, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class SalleDelete(DeleteView):
    template_name = 'salles/salle_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Salle, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')

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
    template_name = 'semestres/semestre_create.html'
    form_class = SemestreModelForm
    queryset = Semestre.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class SemestreList(ListView):
    template_name = 'semestres/semestre_list.html'
    queryset = Semestre.objects.all() # <blog>/<modelname>_list.html

class SemestreDetail(DetailView):
    template_name = 'semestres/semestres_detail.html'
    queryset = Semestre.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Semestre, id=id_)

class SemestreUpdate(UpdateView):
    template_name = 'semestres/semestre_create.html'
    form_class = SemestreModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Semestre, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class SemestreDelete(DeleteView):
    template_name = 'semestres/semestre_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Semestre, id=id_)

    def get_success_url(self):
        return reverse('semestres:semestre-list')




