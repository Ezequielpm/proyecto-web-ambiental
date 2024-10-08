# from django.shortcuts import render, redirect
# from .forms import RegistroForm
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder': 'Correo electrónico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder': 'Repite la contraseña'})
        return form
# def registro(request):
#     if request.method == 'POST':
#         form = RegistroForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirigir después del registro exitoso
#     else:
#         form = RegistroForm()
    
#     return render(request, 'registration/registro.html', {'form': form})
