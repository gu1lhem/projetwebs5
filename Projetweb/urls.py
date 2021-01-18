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

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# Views dont on créé les urlpatterns.
from GestionEDT.views import *

# Bootstrap Crud Template
from bsct.urls import URLGenerator

bsct_patterns = URLGenerator( Professeur ).get_urlpatterns(crud_types = 'crudl')
""" Génération automatique de toutes les URLs de création, détails, etc.
   #'c' - Refers to the Create CRUD type
   #'r' - Refers to the Read/Detail CRUD type
   #'u' - Refers to the Update/Edit CRUD type
   #'d' - Refers to the Delete CRUD type
   #'l' - Refers to the List CRUD type
"""

urlpatterns = [
   # Index
   path('', home, name = 'homepage'),
   path('index/', home, name = 'homepage'),
   path('home/', home, name = 'homepage'),

   url( '', include( bsct_patterns ) )
]

"""
urlpatterns = [
   # Index
   path('', home, name = 'homepage'),
   path('index/', home, name = 'homepage'),
   path('home/', home, name = 'homepage'),

   path('admin/', admin.site.urls),

   path('etudiant/', EtudiantList.as_view(), name='etudiant-list'),
   path('etudiant/add/',EtudiantCreate.as_view(),name='etudiant-add'),
   path('etudiant/<int:NumEtudiant>/', EtudiantDetail.as_view(), name='etudiant-detail'),
   path('etudiant/<int:NumEtudiant>/delete/',EtudiantDelete.as_view(),name='etudiant-delete'),
   path('etudiant/<int:NumEtudiant>/update/',EtudiantUpdate.as_view(),name='etudiant-update'),

   path('UC/', UCList.as_view(), name='uc-list'),
   path('UC/add/', UCCreate.as_view(), name='uc-add'),
   path('UC/<int:idUC>/', UCDetail.as_view(), name='uc-detail'),
   path('UC/<int:idUC>/update/', UCUpdate.as_view(), name='uc-update'),
   path('UC/<int:idUC>/delete/', UCDelete.as_view(), name='uc-delete'),

   path('salle/', SalleList.as_view(), name='salle-list'),
   path('salle/add/', SalleCreate.as_view(), name='salle-add'),
   path('salle/<int:idSalle>/', SalleDetail.as_view(), name='salle-detail'), # clés primaires de 
   path('salle/<int:idSalle>/update/', SalleUpdate.as_view(), name='salle-update'), # salle ?
   path('salle/<int:idSalle>/delete/', SalleDelete.as_view(), name='salle-delete'),

   path('seance/', SeanceList.as_view(), name='seance-list'),
   path('seance/add/', SeanceCreate.as_view(), name='seance-add'),
   path('seance/<int:idSeance>/', SeanceDetail.as_view(), name='seance-detail'),
   path('seance/<int:idSeance>/update/', SeanceUpdate.as_view(), name='seance-update'),
   path('seance/<int:idSeance>/delete/', SeanceDelete.as_view(), name='seance-delete'),

   path('groupe/', GroupeList.as_view(), name='groupe-list'),
   path('groupe/add/', GroupeCreate.as_view(), name='groupe-add'),
   path('groupe/<int:idGroupe>/', GroupeDetail.as_view(), name='groupe-detail'),
   path('groupe/<int:idGroupe>/update/', GroupeUpdate.as_view(), name='groupe-update'),
   path('groupe/<int:idGroupe>/delete/', GroupeDelete.as_view(), name='groupe-delete'),

   path('formation/', FormationList.as_view(), name='formation-list'),
   path('formation/add/', FormationCreate.as_view(), name='formation-add'),
   path('formation/<int:idFormation>/', FormationDetail.as_view(), name='formation-detail'),
   path('formation/<int:idFormation>/update/', FormationUpdate.as_view(), name='formation-update'),
   path('formation/<int:idFormation>/delete/', FormationDelete.as_view(), name='formation-delete'),
]

urlpatterns += [
   path('accounts/', include('django.contrib.auth.urls')),
]
"""