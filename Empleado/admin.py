from django.contrib import admin
from django.urls import clear_script_prefix

from .models import LeadTeam
from .models import Colaborador

admin.site.register(LeadTeam)
admin.site.register(Colaborador)

