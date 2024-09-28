from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente tras el registro
            return redirect('nombre_de_la_vista_principal')  # Cambia 'nombre_de_la_vista_principal' por la vista a la que quieras redirigir
    else:
        form = RegistroForm()

    return render(request, 'registration/registro.html', {'form': form})
