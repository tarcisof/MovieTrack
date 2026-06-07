from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class Login(View):
    def get (self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect('listar_filmes')
        return render(request, 'login.html', contexto)
        
    def post (self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('listar_filmes')
            else:
                return render(request, 'login.html', {'mensagem': 'Usuário inativo'})
        else:
            return render(request, 'login.html', {'mensagem': 'Usuário ou senha inválidos.'})
        
class Cadastro(View):
    def get(self, request):
        return render(request, 'cadastro.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            return render(request, 'cadastro.html', {'mensagem': 'As senhas não coincidem.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'cadastro.html', {'mensagem': 'Este nome de usuário já está em uso.'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return redirect('login')
        
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')