from django.db import models
from modelcluster.fields import ParentalKey
from ls.joyous.models import (MultidayEventPage, RecurringEventPage,
                              MultidayRecurringEventPage, removeContentPanels,
                              )
from ls.joyous.models.one_off_events import SimpleEventPage
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.core.models import Orderable
from GestionEDT.models import *

# Hide unwanted event types
MultidayEventPage.is_creatable = False
RecurringEventPage.is_creatable = False
MultidayRecurringEventPage.is_creatable = False

#Intégration de champ relatif à nos models Professeur, Groupe d'étudiants, etc..
#SimpleEventPage.content_panels += [MultiFieldPanel('Professeur')]
class SimpleRelatedEventPage(Orderable,SimpleEventPage):
    id_seance = models.AutoField("Identifiant de la séance",primary_key=True)   
    professeur = ParentalKey(Professeur, on_delete=models.CASCADE, related_name='professeur')
    groupe = ParentalKey(Groupe,on_delete=models.CASCADE, related_name='groupe')
    salle = ParentalKey(Salle, on_delete=models.CASCADE, related_name='salle')
    uc = ParentalKey(UC,on_delete=models.CASCADE, related_name='matière')

    content_panels = [
    InlinePanel('professeur', label="Professeur animant le cours"),
    InlinePanel('groupe', label="Groupe assistant au cours"),
    InlinePanel('salle', label="Salle dans laquelle se déroule le cours"),
    InlinePanel('matière', label="Matière du cours"),
]


