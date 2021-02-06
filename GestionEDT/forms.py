from django import forms
from .models import (
    Etudiant,
    Professeur,
    UC,
    Salle,
    Groupe,
    Seance,
    Formation,
    SeanceOccurence
)
from schedule.forms import SpanForm


class Form_import_fichier(forms.Form):
    fichier = forms.FileField()


class SeanceAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Seance


class SeanceOccurrenceForm(SpanForm):
    class Meta:
        model = SeanceOccurence
        exclude = ("original_start", "original_end", "event", "cancelled")
