
from django.urls import path
from LoginApp.views import renderlogin

urlpatterns = [
    path('', renderlogin)
]