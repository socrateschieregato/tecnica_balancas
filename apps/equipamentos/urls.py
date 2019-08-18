from django.urls import path

from apps.equipamentos import views

urlpatterns = [
    path('', views.equip_home, name='equip_home'),
    path('cad_equip/', views.cad_equip, name='cad_equip')
]
