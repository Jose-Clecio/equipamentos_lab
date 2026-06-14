from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipamentos, name='equipamentos'),
    path('caracteristicas/<int:id>/', views.caracteristica, name='caracteristicas')
]