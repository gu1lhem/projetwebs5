from GestionEDT.forms import SeanceAdminForm
from django.contrib import admin
from schedule.admin import *
from GestionEDT.models import Seance, SeanceOccurence


# Register your models here.
@admin.register(Seance)
class SeanceAdmin(EventAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": [
                    'timecode_debut', 'timecode_fin', 'fk_professeur', 'fk_groupe', 'fk_uc', 'fk_salle'
                ]
            },
        ),
    )
    form = SeanceAdminForm


admin.site.register(SeanceOccurence, admin.ModelAdmin)
