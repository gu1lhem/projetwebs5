"""projectwebs5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
   1. Add an import:  from my_app import views
   2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
   1. Add an import:  from other_app.views import Home
   2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
   1. Import the include() function: from django.urls import include, path
   2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from StudentManager import views
from StudentManager.views import *


urlpatterns = [
   path('', views.index, name='home'),
   path('home/', home, name = 'homepage'),
   path('other/', other, name = 'otherpage'),
   path('admin/', admin.site.urls),
   path('perso/', perso, name = 'perso'),
   path('persoX/<int:id>', persoX, name = 'persoX'),   
   path('ec/', ec, name = 'ec'),
   path('ecX/<int:id>', ecX, name = 'ecX'),
   path('RechercheNom', RechercheNom, name = 'RechercheNom'), 
   path('get_name/', get_name, name = 'get_name'),
   path('ajax_calls/search/', autocompleteModel, name = 'autocompleteModel'),
]
urlpatterns += [
   path('accounts/', include('django.contrib.auth.urls')),
]
