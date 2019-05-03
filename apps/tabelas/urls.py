from django.urls import path, include
from apps.tabelas import views


urlpatterns = [
    path('', views.tabelas_home, name='tabelas_home')
]