from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:obra>', views.equipamentos, name='equipamentos'),
    path('<str:obra>/caracteristicas/<int:id>/', views.caracteristica, name='caracteristicas')
]