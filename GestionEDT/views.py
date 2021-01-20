from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .models import *



def home(request):
   # Le contexte title permet, avec un if dans le template, de spécifier un titre à la page.
   # Si aucun titre n'est spécifié, c'est le titre par défaut 'StudentManager' qui est utilisé.
   return render(request, 'home.html', {'title': 'Bienvenue'})


def export_etudiant_csv(request):
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="etudiants.csv"'

   writer = csv.writer(response)
   writer.writerow(['NumEtudiant','Prenom','Nom','Adressemail','Naiss'])

   etudiant = Etudiant.objects.all().values_list('NumEtudiant','Prenom','Nom','Adressemail','Naiss')
   for etudiants in etudiant:
      writer.writerow(etudiants)  

   return response

def import_etudiant(request):
    # declaring template
    template = "etudiant_import.html"
    data = Etudiant.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Ordre dans le csv devrait etre numEtudiant, prenom, Nom, addressemail, Date de Naissance, Niveau et Groupe',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "Ce n'est pas un fichier csv")
    data_set = csv_file.read().decode('UTF-8')
io_string = io.StringIO(data_set)
next(io_string)
for column in csv.reader(io_string, delimiter=',', quotechar="|"):
      , created = Etudiant.objects.update_or_create(
        NumEtudiant=column[0],
        Prenom=column[1],
        addressemail=column[2],
        Naiss=column[3],
        Niveau=column[4],
        fk_Groupe=column[5]
    )
context = {}
return render(request, template, context)
