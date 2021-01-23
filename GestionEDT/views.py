from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .import utilitaire

from .models import *



def home(request):
   # Le contexte title permet, avec un if dans le template, de spécifier un titre à la page.
   # Si aucun titre n'est spécifié, c'est le titre par défaut 'StudentManager' qui est utilisé.
   return render(request, 'home.html', {'title': 'Bienvenue'})



def export_etudiant_csv(request):
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="etudiants.csv"'

   writer = csv.writer(response)
   writer.writerow(['num_etudiant','prenom','nom','adresse_courriel','date_naissance','niveau','fk_groupe'])

   etudiant = Etudiant.objects.all().values_list('num_etudiant','prenom','nom','adresse_courriel','date_naissance','niveau','fk_groupe')
   for etudiants in etudiant:
      writer.writerow(etudiants)  
   return response

def import_fichier(requete):
    contexte = {
        'titre': 'Import fichier',
        'formulaire': Form_import_fichier()
    }

    if requete.method == 'POST':
        formulaire = Form_import_fichier(requete.POST, requete.FILES)
        if formulaire.is_valid():
            fichier = requete.FILES['fichier']
            if not fichier.name.endswith('.csv'):
                messages.warning(requete, 'le fichier n\'est pas un csv !')

            else:
                donnees = fichier.read().decode('UTF-8')
                erreurs, total = utilitaire.traitement_fichier(donnees)
                if total == erreurs:
                    messages.warning(requete, 'Echec de l\'import !\n')

                else:
                    messages.success(requete, f'Import effectue ! {erreurs} erreur(s)\n')
                    return redirect('home')
                
        else:
            messages.warning(requete, 'Erreur lors de l\'import !\n')
    
    return render(requete, 'etudiants/etudiant_import.html', contexte)






