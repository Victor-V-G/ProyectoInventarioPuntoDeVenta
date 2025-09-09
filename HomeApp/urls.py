from django.urls import path
from HomeApp.views import renderTemplateHome

urlpatterns = [
    path('', renderTemplateHome)
]