from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')

        usuario = authenticate(request, username=usuario, password=contrasena)

        if usuario is not None:
            login(request, usuario)
            return redirect('main')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
        
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def main(request):
    return render(request, 'main.html')