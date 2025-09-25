from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Sistema de Pedidos no ar 🚀</h1><p>Bem-vindo!</p>")


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("app_principal/", include("app_principal.urls")),
    # demais rotas...
]
