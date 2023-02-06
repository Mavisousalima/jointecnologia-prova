from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import folium

from .models import Alvo
from .forms import AlvoForm


def index(request):
    lat = '-14.2350'
    long = '-51.9253'

    alvos = Alvo.objects.all()
    mapa = folium.Map(location=[lat, long], zoom_start=3)

    for alvo in alvos:
        iframe = f"<div><h1>{alvo.nome}</h1><p>Lat: {alvo.latitude}</p><p>Long: {alvo.longitude}</p><p>Data Exp: {alvo.data_expiracao}</p><a href='atualizar_alvo/{alvo.identificador}'><button class='btn btn-warning'>Atualizar</button></a><p></p><a href='remover_alvo/{alvo.identificador}'><button class='btn btn-danger'>Excluir</button></a></div>"
        mapa.add_child(folium.Marker(location=[alvo.latitude, alvo.longitude], popup=folium.Popup(iframe, max_width=200), icon=folium.Icon(color='green')))

    mapa.save("alvo/templates/includes/map.html")
    return render(request, 'index.html')


def criar_alvo(request):
    if request.method == 'POST':
        form = AlvoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AlvoForm()
    
    return render(request, 'alvo_form.html', {'form': form})


def atualiza_alvo(request, pk):
     alvo_obj = get_object_or_404(Alvo, pk=pk)
     if request.method == 'POST':
         form = AlvoForm(instance=alvo_obj, data=request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect(reverse('index'))
     else:
         form = AlvoForm(instance=alvo_obj)

     return render(request, "alvo_form.html", { "form": form, "object": alvo_obj})


def remove_alvo(request, pk):
     alvo_obj = get_object_or_404(Alvo, pk=pk)
     alvo_obj.delete()
     return HttpResponseRedirect(reverse('index'))