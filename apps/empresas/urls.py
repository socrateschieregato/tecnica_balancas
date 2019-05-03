from django.urls import path, include
from apps.empresas import views

urlpatterns = [
    path('', views.empresas_home, name='empresas_home')
]