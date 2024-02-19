from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def crear_elegir_receta(request):
    return render(request, 'Crear_Elegir_Receta.html')

def olvido_contraseña(request):
    return render(request, 'Olvido_Contraseña.html')

def inicio_sesion_registro(request):
    return render(request, 'Inicio_Sesion_Registro.html')

def salud_nutricion(request):
    return render(request, 'Salud_y_Nutricion.html')

def calculadora_salud(request):
    return render(request, 'Calculadora_De_Salud.html')