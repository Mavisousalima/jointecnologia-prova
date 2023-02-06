from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('adicionar/', views.criar_alvo, name="adiciona_alvo"),
    path('remover_alvo/<int:pk>', views.remove_alvo, name='remover_alvo'),
    path('atualizar_alvo/<int:pk>', views.atualiza_alvo, name='atualiza_alvo'),
]