from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from movies.models import Filme
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from movies.forms import FilmeForm

class ListarFilmes(LoginRequiredMixin, ListView):
    model = Filme
    template_name = 'filmes/listar_filmes.html'
    context_object_name = 'filmes'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar', '')
        if buscar:
            return self.model.objects.filter(usuario=self.request.user, titulo__icontains=buscar)
        return self.model.objects.filter(usuario=self.request.user)
    
class CriarFilme(LoginRequiredMixin, CreateView):
    model = Filme
    template_name = 'filmes/criar_filme.html'
    success_url = reverse_lazy('listar_filmes')
    form_class = FilmeForm

class EditarFilme(LoginRequiredMixin, UpdateView):
    model = Filme
    template_name = 'filmes/editar_filme.html'
    success_url = reverse_lazy('listar_filmes')
    form_class = FilmeForm

    def get_queryset(self):
        return self.model.objects.filter(usuario=self.request.user)

class DeletarFilme(LoginRequiredMixin, DeleteView):
    model = Filme
    template_name = 'filmes/deletar_filme.html'
    success_url = reverse_lazy('listar_filmes')

    def get_queryset(self):
        return self.model.objects.filter(usuario=self.request.user)

class Capa(LoginRequiredMixin, View):
    def get(self, request, filename):
        try:
            filme = Filme.objects.filter(capa='capas/{}'.format(filename)).first()
            if filme and filme.capa:
                return FileResponse(filme.capa.open(), content_type='image/jpeg')
            else:
                return HttpResponseNotFound('Capa não encontrada')
        except Exception as e:
            raise HttpResponseNotFound('Erro ao carregar a capa: {}'.format(str(e)))