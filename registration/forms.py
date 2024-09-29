from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True,help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta():
        model = User
        fields = ("username","email","password1","password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado. Prueba con otro.")
        return email    
# class RegistroForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         # Sobrescribe el método save para asegurarse de que el correo se guarde
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']  # Asigna el correo del formulario al campo email del usuario
#         if commit:
#             user.save()
#         return user
