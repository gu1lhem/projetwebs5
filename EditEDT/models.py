from operator import add
from django.db import models
from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey, EmailField

from ls.joyous.models import (MultidayEventPage, RecurringEventPage,
                              MultidayRecurringEventPage, removeContentPanels,
                              )
from ls.joyous.models.one_off_events import SimpleEventPage
from wagtail.admin.edit_handlers import MultiFieldPanel
from GestionEDT.models import *

# Hide unwanted event types
MultidayEventPage.is_creatable = False
RecurringEventPage.is_creatable = False
MultidayRecurringEventPage.is_creatable = False

#Intégration de champ relatif à nos models Professeur, Groupe d'étudiants, etc..
#SimpleEventPage.content_panels += [MultiFieldPanel('Professeur')]

# Hide unwanted content
removeContentPanels(["image","category", "tz", "group_page", "website"])
# Create your models here.
