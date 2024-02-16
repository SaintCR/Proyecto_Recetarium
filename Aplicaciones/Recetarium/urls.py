from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crear-elegir-receta/', views.crear_elegir_receta),
    path('recuperacion-de-contraseña/', views.olvido_contraseña),
]