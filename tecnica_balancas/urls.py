from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('apps.home.urls')),
    path('calibracoes/', include('apps.calibracoes.urls')),
    path('tabelas/', include('apps.tabelas.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('equipamentos/', include('apps.equipamentos.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
