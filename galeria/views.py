from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia


def index(request):

    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards":fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # ou traz o objeto ou erro
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia}) # após, definir ainda a rota