from django.contrib import admin

from .models import Si_Statut
from .models import Si_Personnel
from .models import Si_View_Ls

admin.site.register(Si_Statut)
admin.site.register(Si_Personnel)
admin.site.register(Si_View_Ls)
