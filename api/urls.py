from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet)
router.register(r"imoveis", ImovelViewSet)
router.register(r"pagamentos", PagamentoViewSet)
router.register(r"contratos", ContratoViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_par'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

""" path('imoveis', ImovelView.as_view()),
    path('imoveis/<int:pk>', ImovelDetailView.as_view()),

    path('contratos', ContratoView.as_view()),
    path('contratos/<int:pk>', ContratoDetailView.as_view()),

    path('pagamentos', PagamentoView.as_view()),
    path('pagamentos/<int:pk>', PagamentoDetailView.as_view()),

"""

"""path('users', UsuarioView.as_view()),
    path('usuario/<int:pk>', UsuarioDetailView.as_view()),

    path('imoveis', ImovelView.as_view()),
    path('imovel/<int:pk>', ImovelDetailView.as_view()),

    path('contratos', ContratoView.as_view()),
    path('contrato/<int:pk>', ContratoDetailView.as_view()),

    path('pagamentos', PagamentoView.as_view()),
    path('pagamento/<int:pk>', PagamentoDetailView.as_view()),
"""