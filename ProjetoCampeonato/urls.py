"""ProjetoCampeonato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path, include

import Jogadores.urls
import Jogos.urls
import Juizes.urls
import Pages
import Times.urls
import  Campos.urls
import Usuarios.urls
import Pages.urls
from Campos.urls import urlpatterns
from Times.urls import urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(Pages.urls.urlspatterns)),
    path('', include(Times.urls.urlpatterns)),
    path('', include(Campos.urls.urlpatterns)),
    path('', include(Juizes.urls.urlpatterns)),
    path('', include(Jogadores.urls.urlpartterns)),
    path('', include(Usuarios.urls.urlpatterns)),
    path('', include(Jogos.urls.urlspatterns)),

]

