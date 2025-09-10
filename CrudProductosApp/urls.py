from django.urls import path
from CrudProductosApp.views import renderTemplateCrudProductos


urlpatterns = [
    path('', renderTemplateCrudProductos),
]