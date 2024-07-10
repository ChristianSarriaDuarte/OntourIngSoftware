from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registrarExcursion/', views.registrarExcursion),
    path('edicionExcursion/<codigo>', views.edicionExcursion),
    path('editarExcursion/', views.editarExcursion),
    path('eliminarExcursion/<codigo>', views.eliminarExcursion)
   
]