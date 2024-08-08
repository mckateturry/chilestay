from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Inmueble, TipoUsuario, Region

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

#fields = ['nombres', 'apellidos']




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'direccion', 'telefono', 'tipo_usuario', 'correo_electronico']


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['id', 'nombre', 'arrendada', 'direccion', 'comuna', 'region', 'tipo_inmueble', 'servicios', 'calificacion_sernatur', 'telefono', 'correo_electronico', 'pagina_web', 'descripcion', 'foto', 'fecha_disponible_desde', 'fecha_disponible_hasta', 'capacidad_adultos']
        widgets = {
            'servicios': forms.Textarea(attrs={'rows': 3}),
            'calificacion_sernatur': forms.Textarea(attrs={'rows': 3}),
        }
        
class FiltroInmuebleForm(forms.Form):
    ZONAS = [
        ('', 'Seleccionar Zona'),
        ('norte', 'Zona Norte'),
        ('centro', 'Zona Centro'),
        ('sur', 'Zona Sur'),
        ('austral', 'Zona Austral'),
    ]

    zona = forms.ChoiceField(choices=ZONAS, required=False, label='Zona')
    llegada = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Seleccionar fecha'}), required=False, label='Llegada')
    salida = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Seleccionar fecha'}), required=False, label='Salida')
    adultos = forms.IntegerField(min_value=0, initial=0, required=False, label='Adultos')
    niños = forms.IntegerField(min_value=0, initial=0, required=False, label='Niños')
    bebes = forms.IntegerField(min_value=0, initial=0, required=False, label='Bebés')
    mascotas = forms.IntegerField(min_value=0, initial=0, required=False, label='Mascotas')
# #REGISTRAR INMUEBLES
# class InmuebleForm(forms.ModelForm):
#     class Meta:
#         model = Inmueble
#         fields = [
#             'id', 'nombre', 'arrendada', 'direccion', 'comuna', 'region', 'tipo_inmueble',
#             'servicios', 'calificacion_sernatur', 'telefono', 'correo_electronico',
#             'pagina_web', 'descripcion', 'usuarios', 'fecha_disponible_desde',
#             'fecha_disponible_hasta', 'capacidad_adultos'
#         ]
#         widgets = {
#             'fecha_disponible_desde': forms.DateInput(attrs={'type': 'date'}),
#             'fecha_disponible_hasta': forms.DateInput(attrs={'type': 'date'}),
#         }
