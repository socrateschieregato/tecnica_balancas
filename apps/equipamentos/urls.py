from django.urls import path

from apps.equipamentos import views

urlpatterns = [
    path('', views.equip_home, name='equip_home'),
    path('cad_equip/', views.cad_equip, name='cad_equip'),
    path('del_equip/<int:id>', views.del_equip, name='del_equip'),
    path('upd_equip/<int:id>', views.upd_equip, name='upd_equip')
]
