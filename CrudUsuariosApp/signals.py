from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from .models import Usuarios

APP_LABEL = "CrudUsuariosApp"

@receiver(post_migrate)
def CrearUsuarioAdminDefault(sender, **kwargs):

    if getattr(sender, "label", None) != APP_LABEL:
        return
    
    if not Usuarios.objects.filter(Username="Admin").exists():
        Usuarios.objects.create(
            Username="Admin",
            Password=make_password("Admin123"),
            ConfirmarPassword="Admin123",
            CorreoElectronico="admin@gmail.com",
        )
        print("Usuario admin creado con éxito automáticamente")
