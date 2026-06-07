# movies/forms.py
from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'capa', 'diretor', 'ano_lancamento', 'genero', 'assistido', 'nota', 'comentario_pessoal']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'diretor': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_lancamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'assistido': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'comentario_pessoal': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }