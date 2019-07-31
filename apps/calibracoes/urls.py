from django.urls import path, include
from apps.calibracoes import views


urlpatterns = [
    path('', views.calib_home, name='calib_home'),
    path('list_calib/', views.list_calib, name='list_calib'),
    path('cad_calib/', views.cad_calib, name='cad_calib')
]