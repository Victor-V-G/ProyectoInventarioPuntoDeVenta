from django.contrib import admin

from .models import (
    AuditoriaBodega,
    AuditoriaCargo,
    AuditoriaCategoria,
    AuditoriaEmpleado,
    AuditoriaProducto,
    AuditoriaUsuario
)

# =============================================================================
# BASE ADMIN SOLO LECTURA (SIN AGREGAR / EDITAR / ELIMINAR)
# =============================================================================
class AuditoriaBaseAdmin(admin.ModelAdmin):

    # Bloquear agregar
    def has_add_permission(self, request):
        return False

    # Bloquear editar
    def has_change_permission(self, request, obj=None):
        return False

    # Bloquear eliminar
    def has_delete_permission(self, request, obj=None):
        return False

    # Quitar acciones "Eliminar seleccionados"
    actions = None

    # Configuración común
    list_per_page = 10


# =============================================================================
# AUDITORÍA BODEGA
# =============================================================================
class AuditoriaBodegaAdmin(AuditoriaBaseAdmin):

    # Campos de la tabla principal
    list_display = [
        "IdAuditoriaBodega",
        "Accion",
        "BodegaIdRespaldo",
        "BodegaNombreRespaldo",
        "Fecha_hora",
    ]

    # Filtros laterales
    list_filter = ["Accion", "Fecha_hora"]

    # Campos buscables
    search_fields = [
        "IdAuditoriaBodega",
        "Accion",
        "BodegaIdRespaldo",
        "BodegaNombreRespaldo",
    ]

    # Campos detalle
    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Bodega', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('BodegaIdRespaldo', 'BodegaNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaBodega',
        'Bodega',
        'Usuario',
        'BodegaIdRespaldo',
        'BodegaNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA CARGO
# =============================================================================
class AuditoriaCargoAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaCargo",
        "Accion",
        "CargoIdRespaldo",
        "CargoNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaCargo",
        "Accion",
        "CargoIdRespaldo",
        "CargoNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Cargo', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('CargoIdRespaldo', 'CargoNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaCargo',
        'Cargo',
        'Usuario',
        'CargoIdRespaldo',
        'CargoNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA CATEGORÍA
# =============================================================================
class AuditoriaCategoriaAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaCategoria",
        "Accion",
        "CategoriaIdRespaldo",
        "CategoriaNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaCategoria",
        "Accion",
        "CategoriaIdRespaldo",
        "CategoriaNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Categoria', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('CategoriaIdRespaldo', 'CategoriaNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaCategoria',
        'Categoria',
        'Usuario',
        'CategoriaIdRespaldo',
        'CategoriaNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA EMPLEADO
# =============================================================================
class AuditoriaEmpleadoAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaEmpleado",
        "Accion",
        "EmpleadoIdRespaldo",
        "EmpleadoNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaEmpleado",
        "Accion",
        "EmpleadoIdRespaldo",
        "EmpleadoNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Empleado', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('EmpleadoIdRespaldo', 'EmpleadoNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaEmpleado',
        'Empleado',
        'Usuario',
        'EmpleadoIdRespaldo',
        'EmpleadoNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA PRODUCTO
# =============================================================================
class AuditoriaProductoAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaProducto",
        "Accion",
        "ProductoIdRespaldo",
        "ProductoNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaProducto",
        "Accion",
        "ProductoIdRespaldo",
        "ProductoNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Producto', 'Usuario')
        }),
        ('Respaldo', {
            'fields': ('ProductoIdRespaldo', 'ProductoNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaProducto',
        'Producto',
        'Usuario',
        'ProductoIdRespaldo',
        'ProductoNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# AUDITORÍA USUARIO
# =============================================================================
class AuditoriaUsuarioAdmin(AuditoriaBaseAdmin):

    list_display = [
        "IdAuditoriaUsuario",
        "Accion",
        "UsuarioIdRespaldo",
        "UsuarioNombreRespaldo",
        "Fecha_hora",
    ]

    list_filter = ["Accion", "Fecha_hora"]

    search_fields = [
        "IdAuditoriaUsuario",
        "Accion",
        "UsuarioIdRespaldo",
        "UsuarioNombreRespaldo",
    ]

    fieldsets = (
        ('Datos importantes', {
            'fields': ('Accion', 'Fecha_hora')
        }),
        ('Asociados', {
            'fields': ('Usuario',)
        }),
        ('Respaldo', {
            'fields': ('UsuarioIdRespaldo', 'UsuarioNombreRespaldo')
        }),
    )

    readonly_fields = [
        'IdAuditoriaUsuario',
        'Usuario',
        'UsuarioIdRespaldo',
        'UsuarioNombreRespaldo',
        'Accion',
        'Fecha_hora',
    ]


# =============================================================================
# REGISTROS
# =============================================================================
admin.site.register(AuditoriaBodega, AuditoriaBodegaAdmin)
admin.site.register(AuditoriaCargo, AuditoriaCargoAdmin)
admin.site.register(AuditoriaCategoria, AuditoriaCategoriaAdmin)
admin.site.register(AuditoriaEmpleado, AuditoriaEmpleadoAdmin)
admin.site.register(AuditoriaProducto, AuditoriaProductoAdmin)
admin.site.register(AuditoriaUsuario, AuditoriaUsuarioAdmin)
