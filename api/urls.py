from django.contrib import admin
from django.urls import path, include
from api.views import *

urlpatterns = [
    path('usuarios', listUsers),
    path('users', UsuarioView.as_view()),
    path('usuario/<int:pk>', UsuarioDetailView.as_view()),

    path('imoveis', ImovelView.as_view()),
    path('imoveis/<int:pk>', ImovelDetailView.as_view()),

    path('contratos', ContratoView.as_view()),
    path('contratos/<int:pk>', ContratoDetailView.as_view()),

    path('pagamentos', PagamentoView.as_view()),
    path('pagamentos/<int:pk>', PagamentoDetailView.as_view()),
]
