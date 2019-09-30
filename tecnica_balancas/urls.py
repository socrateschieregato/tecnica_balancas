from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('home.urls')),
    path('api/', include('api.urls')),
    path('auth/', obtain_auth_token),
    path('calibracoes/', include('calibracoes.urls')),
    path('tabelas/', include('tabelas.urls')),
    path('empresas/', include('empresas.urls')),
    path('equipamentos/', include('equipamentos.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
