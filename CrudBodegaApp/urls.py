from django.urls import path
from CrudBodegaApp.views import renderTemplateCrudBodega

urlpatterns = [
    path('', renderTemplateCrudBodega),
]