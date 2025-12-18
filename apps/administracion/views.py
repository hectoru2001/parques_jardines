from django.shortcuts import render
from .models import LogSistema
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

@login_required
def gestion_usuarios(request):
    # Solo administradores y supervisores pueden gestionar usuarios
    if not request.user.groups.filter(name__in=["Administrador", "Supervisor"]).exists():
        messages.error(request, "No tienes permisos para acceder a esta sección.")
        return redirect('home')

    users = User.objects.all().order_by('username')
    grupos = Group.objects.all()

    # Identificar roles del usuario actual
    es_administrador = request.user.groups.filter(name="Administrador").exists()
    es_supervisor = request.user.groups.filter(name="Supervisor").exists()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action in ["crear", "editar"]:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            grupos_seleccionados = request.POST.getlist('grupos')

            # Supervisores no pueden asignar grupo Administrador
            if es_supervisor and "Administrador" in grupos_seleccionados:
                grupos_seleccionados.remove("Administrador")
                messages.warning(request, "No puedes asignar el grupo Administrador.")

            if action == "crear":
                if username and password:
                    user = User.objects.create_user(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        password=password
                    )
                    for g in grupos_seleccionados:
                        group = Group.objects.get(name=g)
                        user.groups.add(group)
                    messages.success(request, f"Usuario {username} creado correctamente.")
                else:
                    messages.error(request, "Debe proporcionar usuario y contraseña.")

            elif action == "editar":
                user_id = request.POST.get('user_id')
                user = get_object_or_404(User, pk=user_id)

                # Supervisores no pueden editar administradores
                if es_supervisor and user.groups.filter(name="Administrador").exists():
                    messages.error(request, "No puedes editar un usuario Administrador.")
                    return redirect('gestion_usuarios')

                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                if password:
                    user.set_password(password)

                user.groups.clear()
                for g in grupos_seleccionados:
                    user.groups.add(Group.objects.get(name=g))
                user.save()
                messages.success(request, f"Usuario {user.username} actualizado correctamente.")

        elif action == "eliminar":
            user_id = request.POST.get('user_id')
            user = get_object_or_404(User, pk=user_id)

            if es_supervisor and user.groups.filter(name="Administrador").exists():
                messages.error(request, "No puedes eliminar un usuario Administrador.")
            else:
                user.delete()
                messages.success(request, f"Usuario {user.username} eliminado correctamente.")

        return redirect('gestion_usuarios')

    return render(request, 'usuarios.html', {
        'users': users,
        'grupos': grupos,
        'es_administrador': es_administrador,
        'es_supervisor': es_supervisor
    })

def panel_vista(request):
    return render(request, "panel.html")

def ListadoLogs(request):
    logs = LogSistema.objects.all().order_by('-id')
    return render(request, "logs.html", {'logs':logs})