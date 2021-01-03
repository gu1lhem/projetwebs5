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

class UECreate(CreateView):
    model = UniteEnseignement
    template_name = 'UEs/ue_create.html'
    form_class = UEModelForm
    queryset = UniteEnseignement.objects.all() # <blog>/<modelname>_list.html
    success_url = '/UE'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class UEList(ListView):
    template_name = 'UEs/ue_list.html'
    queryset = UniteEnseignement.objects.all() # <blog>/<modelname>_list.html

class UEDetail(DetailView):
    template_name = 'UEs/ue_detail.html'
    queryset = UniteEnseignement.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("NomMatiere")
        return get_object_or_404(UniteEnseignement, NomMatiere=id_)

class UEUpdate(UpdateView):
    template_name = 'UEs/ue_create.html'
    form_class = UEModelForm

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
        return reverse('etudiants:etudiant-list')

class EtudiantCreate(CreateView):
    model = Etudiant
    template_name = 'etudiants/etudiant_create.html'
    form_class = EtudiantModelForm
    queryset = Etudiant.objects.all() # <blog>/<modelname>_list.html
    success_url = '/etudiant'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class UEList(ListView):
    template_name = 'UEs/ue_list.html'
    queryset = UniteEnseignement.objects.all() # <blog>/<modelname>_list.html

class UEDetail(DetailView):
    template_name = 'UEs/ue_detail.html'
    queryset = UniteEnseignement.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("NomMatiere")
        return get_object_or_404(UniteEnseignement, NomMatiere=id_)

class UEUpdate(UpdateView):
    template_name = 'UEs/ue_create.html'
    form_class = UEModelForm

    def get_object(self):
        id_ = self.kwargs.get("NomMatiere")
        return get_object_or_404(UniteEnseignement, NomMatiere=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
class UEDelete(DeleteView):
    template_name = 'UEs/ue_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("NomMatiere")
        return get_object_or_404(UniteEnseignement, NomMatiere=id_)
        return reverse('ues:ue-list')

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
        return reverse('seances:seance-list')

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
        id_ = self.kwargs.get("idgroupe")
        return get_object_or_404(Formation, id=id_)

class GroupeUpdate(UpdateView):
    template_name = 'groupes/groupe_create.html'
    form_class = GroupeModelForm

    def get_object(self):
        id_ = self.kwargs.get("idgroupe")
        return get_object_or_404(Formation, idgroupe=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
class GroupeDelete(DeleteView):
    template_name = 'groupes/groupe_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("idgroupe")
        return get_object_or_404(Groupe, idgroupe=id_)

    def get_success_url(self):
        return reverse('formation:formation-list')

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
        return reverse('formations:formation-list')

class SemestreCreate(CreateView):
    model = Semestre
    template_name = 'semestres/semestre_create.html'
    form_class = SemestreModelForm
    queryset = Semestre.objects.all() # <blog>/<modelname>_list.html
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class SemestreList(ListView):
    template_name = 'semestres/semestre_list.html'
    queryset = Semestre.objects.all() # <blog>/<modelname>_list.html

class SemestreDetail(DetailView):
    template_name = 'semestres/semestre_detail.html'
    queryset = Semestre.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("NumSemestre")
        return get_object_or_404(Semestre, NumSemestre=id_)

class SemestreUpdate(UpdateView):
    template_name = 'semestres/semestre_create.html'
    form_class = SemestreModelForm

    def get_object(self):
        id_ = self.kwargs.get("NumSemestre")
        return get_object_or_404(Semestre, NumSemestre=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class SemestreDelete(DeleteView):
    template_name = 'semestres/semestre_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("NumSemestre")
        return get_object_or_404(Semestre, NumSemestre=id_)

    def get_success_url(self):
        return reverse('semestres:semestre-list')




