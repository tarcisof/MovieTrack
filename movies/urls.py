from django.urls import path
from movies.views import ListarFilmes, CriarFilme, EditarFilme, DeletarFilme, Capa

urlpatterns = [
    path('', ListarFilmes.as_view(), name='listar_filmes'),
    path('criar/', CriarFilme.as_view(), name='criar_filme'),
    path('editar/<int:pk>/', EditarFilme.as_view(), name='editar_filme'),
    path('deletar/<int:pk>/', DeletarFilme.as_view(), name='deletar_filme'),
    path('fotos/<str:filename>/', Capa.as_view(), name='capa_filmes'),
]