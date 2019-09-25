from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('', include('apps.home.urls')),
    path('api/', include('apps.empresas.urls')),
    path('api/', include('apps.frontend.urls')),
    path('calibracoes/', include('apps.calibracoes.urls')),
    path('tabelas/', include('apps.tabelas.urls')),
    # path('empresas/', include('apps.empresas.urls')),
    path('equipamentos/', include('apps.equipamentos.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
