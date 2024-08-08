from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Inmueble, TipoUsuario

class CrearUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    #nombres = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #apellidos = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rut = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo_electronico = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    tipo_usuario=forms.ModelChoiceField(queryset=TipoUsuario.objects.all(), label="Tipo de Usuario")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Usuario.objects.create(
                user=user,
                #nombres=self.cleaned_data['nombres'],
                #apellidos=self.cleaned_data['apellidos'],
                rut=self.cleaned_data['rut'],
                direccion=self.cleaned_data['direccion'],
                telefono=self.cleaned_data['telefono'],
                correo_electronico=self.cleaned_data['correo_electronico'],
                tipo_usuario=self.cleaned_data['tipo_usuario']
            )
        return user


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['direccion', 'telefono', 'correo_electronico','tipo_usuario']

#fields = ['nombres', 'apellidos', 'direccion', 'telefono_personal', 'correo_electronico']


