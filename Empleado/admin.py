from django.contrib import admin
from django.urls import clear_script_prefix

from .models import Colaborador
from  .models import LiderDeEquipo
from .models import Post

admin.site.register(LiderDeEquipo)
admin.site.register(Colaborador)
admin.site.register(Post)