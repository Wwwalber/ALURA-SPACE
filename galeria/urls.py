from django.urls import path
from galeria.views import index, imagem

# criar lista para manter todos os endpoints relacionados a nossa galeria
urlpatterns = [
    path('', index),
    path('imagem/', imagem)
]