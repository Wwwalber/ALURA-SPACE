from django.urls import path
from galeria.views import index

# criar lista para manter todos os endpoints relacionados a nossa galeria
urlpatterns = [
    path('', index)
]