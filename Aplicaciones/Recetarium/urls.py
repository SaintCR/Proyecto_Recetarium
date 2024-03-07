from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('crear-elegir-receta/', views.crear_elegir_receta, name='crear_elegir_receta'),
    path('recuperacion-de-contraseña/', views.olvido_contraseña, name='olvido_contraseña'),
    path('inicio-sesion-registro/', views.inicio_sesion_registro, name='inicio_sesion_registro'),
    path('salud-nutricion/', views.salud_nutricion, name='salud_nutricion'),
    path('calculadora-salud/', views.calculadora_salud, name='calculadora_salud'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Agrega aquí otras URLs según sea necesario
]
