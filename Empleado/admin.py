from django.contrib import admin
from django.urls import clear_script_prefix

from .models import Colaborador
from  .models import LiderDeEquipo

admin.site.register(LiderDeEquipo)
admin.site.register(Colaborador)

