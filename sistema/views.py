from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

class Login(View):
    def get (self, request):
        contexto = {"Mensagem": "Bem-vindo ao sistema!"}
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'login.html', contexto)
        
    def post (self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                contexto = {"Mensagem": "Usuário inativo."}
                return render(request, 'login.html', contexto)
        else:
            contexto = {"Mensagem": "Usuário ou senha inválidos."}
            return render(request, 'login.html', contexto)
        
class Cadastro(View):
    def get(self, request):
        return render(request, 'cadastro.html')
        
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')