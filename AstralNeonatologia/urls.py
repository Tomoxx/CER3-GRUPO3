"""AstralNeonatologia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth import views as auth_views

from core.api.router import router_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('mapa', views.map, name="map"),
    path('evoluciones/', views.evoluciones, name="evoluciones"),
    path('reciennacidos/', views.reciennacidos, name="reciennacidos"),
    path('login/', views.user_login, name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name="user-logout"),
    path('api/', include(router_posts.urls))
]
