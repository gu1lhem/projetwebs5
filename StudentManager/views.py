from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

import datetime

from StudentManager.models import Si_Personnel
from StudentManager.models import Si_View_Ls
from StudentManager.models import Si_Statut
from StudentManager.models import Si_Ec

from StudentManager.forms import SelectNom

from django.contrib.auth.decorators import login_required


def home(request):
   # Le contexte title permet, avec un if dans le template, de spécifier un titre à la page.
   # Si aucun titre n'est spécifié, c'est le titre par défaut 'StudentManager' qui est utilisé.
   return render(request, 'layout.html', {'title': 'Bienvenue'})

# @login_required
def perso(request):
   personnels = Si_Personnel.objects.all()
   return render(request, 'perso.html',{'personnels': personnels})

def persoX(request, id):
   perso = Si_Personnel.objects.filter(id=id).get()
   minH = Si_Statut.objects.filter(id=perso.fid_statut).get().nb_h_min
   service = Si_View_Ls.objects.filter(fid_pers=id)
   TOTAL = 0
   for ls in service :
      TOTAL += ls.hetd
   return render(request, 'persoX.html', {'personnel': perso, 'services': service, 'minH': minH, 'H_SUP': TOTAL-minH})

def ec(request):
   ECs = Si_Ec.objects.all()
   return render(request, 'ec.html',{'ECs': ECs})

def ecX(request, id):
   ec = Si_Ec.objects.filter(id=id).get()
   service = Si_View_Ls.objects.filter(fid_ec=id).order_by('groupe')   
   return render(request, 'ecX.html', {'EC': ec, 'services': service})

def RechercheNom(request):
   if request.GET.get('q'):
      q = request.GET['q']
      data = Si_Personnel.objects.using('legacy').filter(nom__startswith=q).values_list('nom',flat=True)
      json = list(data)
      return JsonResponse(json, safe=False)
   else:
      ECs = Si_Ec.objects.all()
      return render(request, 'recherche_nom.html') 


def get_name(request): 
   personnels = Si_Personnel.objects.all()
   return render(request, 'recherche_nom.html',{'personnels': personnels})

def autocompleteModel(request):
   if request.is_ajax():
      q = request.GET.get('term', '').capitalize()
      print(q)
      data = Si_Personnel.objects.using('legacy').filter(nom__startswith=q).values_list('nom',flat=True)
      json = list(data)
      return JsonResponse(json, safe=False)
   else:
      data = ''
   mimetype = 'application/json'
   return HttpResponse(data, mimetype) 
