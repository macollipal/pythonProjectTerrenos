"""Terrenos URL Configuration

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
# from django.contrib.auth import views as auth_views  # para_autenticacion
from django.contrib import admin


from django.urls import path

from django.conf.urls import include

from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views


from django.conf.urls.static import static

# from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('index/', include('webapp.urls')),
    path('', include('webapp.urls')),

    path('CorteList/api', views.CorteList.as_view()),
    path('ExisteList/api', views.ExisteList.as_view()),
    path('UbicacionList/api', views.UbicacionList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

