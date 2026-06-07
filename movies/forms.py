# movies/forms.py
from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'capa', 'diretor', 'ano_lancamento', 'genero', 'assistido', 'nota', 'comentario_pessoal']