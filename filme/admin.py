from django.contrib import admin
from .models import Filme

# Register your models here.

# Importar o app Filme aqui no admin para aparecer no admin
admin.site.register(Filme)
