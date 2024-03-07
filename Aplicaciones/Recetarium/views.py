from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    # Your view logic here
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Cambia 'home' por el nombre de tu vista de inicio
        else:
            return render(request, 'login.html', {'error_message': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Cambia 'login' por el nombre de tu vista de login
