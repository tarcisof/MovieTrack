from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout, Cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('logout/', Logout.as_view(), name='logout'),
    path('filmes/', include('movies.urls')),
]
