from django.urls import path, include
from apps.calibracoes import views


urlpatterns = [
    path('', views.calibracoes_home, name='calibracoes_home')
]