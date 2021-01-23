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
from django.conf import settings
from django.conf.urls.static import static

# Views dont on créé les urlpatterns.
from GestionEDT.views import *

# Bootstrap Crud Template
from bsct.urls import URLGenerator

# Wagtail
# https://docs.wagtail.io/en/stable/getting_started/integrating_into_django.html
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

""" Génération automatique de toutes les URLs de création, détails, etc.
   #'c' - Refers to the Create CRUD type
   #'r' - Refers to the Read/Detail CRUD type
   #'u' - Refers to the Update/Edit CRUD type
   #'d' - Refers to the Delete CRUD type
   #'l' - Refers to the List CRUD type
"""
bsct_patterns_p = URLGenerator( Professeur ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_e = URLGenerator( Etudiant ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_u = URLGenerator( UC ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_sa = URLGenerator( Salle ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_se = URLGenerator( Seance ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_g = URLGenerator( Groupe ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_f = URLGenerator( Formation ).get_urlpatterns(crud_types = 'crudl')

urlpatterns = [
   # Index
   path('', home, name = 'homepage'),
   path('index/', home, name = 'homepage'),
   path('home/', home, name = 'homepage'),

   url( '', include( bsct_patterns_p ) ),
   url( '', include( bsct_patterns_e ) ), 
   url( '', include( bsct_patterns_u ) ), 
   url( '', include( bsct_patterns_sa ) ), 
   url( '', include( bsct_patterns_se ) ), 
   url( '', include( bsct_patterns_g ) ), 
   url( '', include( bsct_patterns_f ) ),

   # Wagtail
   path('cms/', include(wagtailadmin_urls)),
      # wagtailadmin_urls provides the admin interface for Wagtail. 
      # This is separate from the Django admin interface (django.contrib.admin); 
      # Wagtail-only projects typically host the Wagtail admin at /admin/, but if 
      # this would clash with your project’s existing admin backend then an alternative path can be used, such as /cms/ here
   path('documents/', include(wagtaildocs_urls)),
      # wagtaildocs_urls is the location from where document files will be served. 
      # This can be omitted if you do not intend to use Wagtail’s document management features.
   path('pages/', include(wagtail_urls)),
      # wagtail_urls is the base location from where the pages of your Wagtail site will be served. 
      # In the above example, Wagtail will handle URLs under /pages/, leaving the root URL and other 
      # paths to be handled as normal by your Django project. If you want Wagtail to handle the 
      # entire URL space including the root URL, this can be replaced with:
      # re_path(r'', include(wagtail_urls)),

   # The URL paths here can be altered as necessary to fit your project’s URL scheme.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #! in production, you will need to configure your web server to serve files from MEDIA_ROOT.

# A l'installation, exécuter
# $ ./manage.py migrate
# $ ./manage.py collectstatic --no-input
# pour Joyous et Wagtail