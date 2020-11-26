from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

import datetime

from django.contrib.auth.decorators import login_required


def home(request):
   # Le contexte title permet, avec un if dans le template, de spécifier un titre à la page.
   # Si aucun titre n'est spécifié, c'est le titre par défaut 'StudentManager' qui est utilisé.
   return render(request, 'home.html', {'title': 'Bienvenue'})
