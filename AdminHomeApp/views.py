from django.shortcuts import render
from LoginApp.decorators import login_requerido

# Create your views here.
@login_requerido
def renderAdminHome(request):
    return render(request, 'templateAdminHome/adminhome.html')


