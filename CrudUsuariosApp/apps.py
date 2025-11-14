from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.hashers import make_password


def crear_usuario_admin(sender, **kwargs):
    # Importar modelos aquí para evitar AppRegistryNotReady
    from CrudUsuariosApp.models import Usuarios  

    if not Usuarios.objects.filter(Username="Admin").exists():
        Usuarios.objects.create(
            Username="Admin",
            Password=make_password("Admin123"),
            CorreoElectronico="admin@gmail.com",
        )
        print("Usuario creado automáticamente")


class CrudusuariosappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CrudUsuariosApp'

    def ready(self):
        from CrudUsuariosApp.apps import crear_usuario_admin
        post_migrate.connect(crear_usuario_admin, sender=self)
