from GestionEDT.forms import SeanceAdminForm
from django.contrib import admin
from schedule.admin import *
from GestionEDT.models import Seance


# Register your models here.
@admin.register(Seance)
class SeanceAdmin(EventAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": [
                    ("fk_professeur", "fk_salle"),
                ]
            },
        ),
    )
    form = SeanceAdminForm
