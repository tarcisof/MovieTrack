from django.db import models
from django.contrib.auth.models import User

class Filme(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='filmes')
    titulo = models.CharField(max_length=255)
    
    # upload_to='capas/' criará uma pasta chamada "capas" dentro do seu diretório de mídia
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    
    diretor = models.CharField(max_length=255, blank=True, null=True)
    ano_lancamento = models.IntegerField(blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, null=True)
    assistido = models.BooleanField(default=False)
    nota = models.IntegerField(blank=True, null=True, help_text="Nota pessoal de 1 a 5")
    comentario_pessoal = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_cadastro']

    def __str__(self):
        return f"{self.titulo} (de {self.usuario.username})"