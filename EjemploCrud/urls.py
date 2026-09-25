"""
URL configuration for EjemploCrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from CrudApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('listado_proyecto/',views.listado_proyecto,name='listado_proyecto'),
    path('agregar_proyecto/',views.agregar_proyecto,name='agregar_proyecto'),
    path('eliminar_proyecto/<int:id>',views.eliminar_proyecto),
    path('modificar_proyecto/<int:id>',views.modificar_proyecto)
]
