# Criando as páginas do site
# Tem que cosntruir uma URL, uma View e um Template (parte visual - arquivos de html)

from django.urls import path
from .views import Homepage, Homefilmes

urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes', Homefilmes.as_view()),
]
