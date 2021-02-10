from django import forms
from .models import (Seance, SeanceOccurence)
from schedule.forms import SpanForm


class SeanceAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Seance


class OccurrenceSeanceForm(SpanForm):
    class Meta:
        model = SeanceOccurence
        exclude = ('event', 'cancelled')
