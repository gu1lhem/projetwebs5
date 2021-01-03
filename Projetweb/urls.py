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
from GestionEDT import views
from GestionEDT.views import *

urlpatterns = [
   path('home/', home, name = 'homepage'),
   path('admin/', admin.site.urls),
   path('UE/', UEList.as_view(), name='ue-list'),
   path('UE/add/', UECreate.as_view(), name='ue-add'),
   path('UE/<int:pk>/', UEDetail.as_view(), name='ue-detail'),
   path('UE/<int:pk>/update/', UEUpdate.as_view(), name='ue-update'),
   path('UE/<int:pk>/delete/', UEDelete.as_view(), name='ue-delete'),
   path('salle/', SalleList.as_view(), name='salle-list'),
   path('salle/add/', SalleCreate.as_view(), name='salle-add'),
   path('salle/<int:pk>/', SalleDetail.as_view(), name='salle-detail'),
   path('salle/<int:pk>/update/', SalleUpdate.as_view(), name='salle-update'),
   path('salle/<int:pk>/delete/', SalleDelete.as_view(), name='salle-delete'),
   path('semestre/', SemestreList.as_view(), name='semestre-list'),
   path('semestre/add/', SemestreCreate.as_view(), name='semestre-add'),
   path('semestre/<int:pk>/', SemestreDetail.as_view(), name='semestre-detail'),
   path('semestre/<int:pk>/update/', SemestreUpdate.as_view(), name='semestre-update'),
   path('semestre/<int:pk>/delete/', SemestreDelete.as_view(), name='semestre-delete'),
   path('formation/', FormationList.as_view(), name='formation-list'),
   path('formation/add/', FormationCreate.as_view(), name='formation-add'),
   path('formation/<int:idFormation>/', FormationDetail.as_view(), name='formation-detail'),
   path('formation/<int:pk>/update/', FormationUpdate.as_view(), name='formation-update'),
   path('formation/<int:pk>/delete/', FormationDelete.as_view(), name='formation-delete'),
   path('groupe/', GroupeList.as_view(), name='groupe-list'),
   path('groupe/add/', GroupeCreate.as_view(), name='groupe-add'),
   path('groupe/<int:pk>/', GroupeDetail.as_view(), name='groupe-detail'),
   path('groupe/<int:pk>/update/', GroupeUpdate.as_view(), name='groupe-update'),
   path('groupe/<int:pk>/delete/', GroupeDelete.as_view(), name='groupe-delete'),
   path('seance/', SeanceList.as_view(), name='seance-list'),
   path('seance/add/', SeanceCreate.as_view(), name='seance-add'),
   path('seance/<int:pk>/', SeanceDetail.as_view(), name='seance-detail'),
   path('seance/<int:pk>/update/', SeanceUpdate.as_view(), name='seance-update'),
   path('seance/<int:pk>/delete/', SeanceDelete.as_view(), name='seance-delete'),
]

urlpatterns += [
   path('accounts/', include('django.contrib.auth.urls')),
]
