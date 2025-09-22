from django.shortcuts import render
from .models import LogSistema

# Create your views here.
def ListadoLogs(request):
    logs = LogSistema.objects.all()
    return render(request, "logs.html",
        {
            'logs':logs
        }
        )