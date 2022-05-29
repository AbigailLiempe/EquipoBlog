from django.contrib import admin
from django.urls import clear_script_prefix

from .models import Colaborador
from  .models import Lider
from .models import Post

admin.site.register(Lider)
admin.site.register(Colaborador)
admin.site.register(Post)