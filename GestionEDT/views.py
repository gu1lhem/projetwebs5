from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import csv, io
from django.contrib import messages

from .models import *



def home(request):
   # Le contexte title permet, avec un if dans le template, de spécifier un titre à la page.
   # Si aucun titre n'est spécifié, c'est le titre par défaut 'StudentManager' qui est utilisé.
   return render(request, 'home.html', {'title': 'Bienvenue'})



def export_etudiant_csv(request):
   response = HttpResponse(content_type='text/csv')   

   writer = csv.writer(response)
   writer.writerow(['prenom','nom','adresse_courriel','date_naissance','niveau','fk_groupe'])

   etudiant = Etudiant.objects.all().values_list('prenom','nom','adresse_courriel','date_naissance','niveau','fk_groupe')
   for etudiants in etudiant:
      writer.writerow(etudiants)
   response['Content-Disposition'] = 'attachment; filename="etudiants.csv"'
   return response   
   

def import_fichier(request):
    template = "import_etudiant.html"
    data = Etudiant.objects.all()
    prompt ={'order': 'l\'odre dans le csv devrait etre numero étudiant, prenom, nom, adresse mail, date de naissance, niveau et sa promotion',
        'etudiants': data }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
         messages.error(request, 'Ce n\'est pas un fichier csv')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=';'):
       _, created = Etudiant.objects.update_or_create(
        prenom=column[0],
        nom=column[1],
        adresse_courriel=column[2],
        date_naissance=column[3],
        niveau=column[4],
        fk_groupe_id=column[5]
    )
    context = {}
    return render(request, template, context)