from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import UsuariosInfo
from .utils import registrar_log


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')

        usuario = authenticate(request, username=usuario, password=contrasena)

        if usuario is not None:
            login(request, usuario)

            # Obtener tipo de usuario
            try:
                usuario_info = UsuariosInfo.objects.filter(usuario=usuario).first()
                tipo_usuario = usuario_info.tipo_usuario if usuario_info else 2

                # Guardar globalmente
                request.session['tipo_usuario'] = tipo_usuario

                registrar_log(request, "El usuario inició sesión")

            except UsuariosInfo.DoesNotExist:
                tipo_usuario = 2
            return redirect('main')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
        
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    registrar_log(request, "El usuario cerró sesión")
    return redirect('login')

@login_required
def main(request):
    return render(request, 'main.html')