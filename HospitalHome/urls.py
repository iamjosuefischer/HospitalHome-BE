"""HospitalHome URL Configuration

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
from HospitalHomeBE import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from HospitalHomeBE.views.createFamiliarView import CrearFamiliarView
from django.contrib import admin
from django.urls import path
  
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.CrearUserView.as_view()),
    path('personalSalud/', views.CrearPSaludView.as_view()),
    path('Familiar/', views.CrearFamiliarView.as_view()),
    path('Paciente/', views.CrearPacienteView.as_view()),
    path('SignosVitales/', views.CrearSigVitalesView.as_view()),
    path('ConsultaUsuario/<int:pk>', views.ConsultUserView.as_view()),
    path('ConsultarFamiliar/<int:pk>', views.ConsultFamiliarView.as_view()),
    path('ConsultarPaciente/<int:pk>', views.ConsultPacienteView.as_view())
]