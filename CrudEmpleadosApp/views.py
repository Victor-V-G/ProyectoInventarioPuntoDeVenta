from django.shortcuts import render
from CrudEmpleadosApp.models import Empleados

# Create your views here.
def renderCrudEmpleados(request):
    return render(request, 'templateCrudEmpleado/crudempleado.html')


def renderTemplateFormularioAgregarEmpleado(request):
    return render(request, 'templateCrudEmpleado/formularioempleado.html')

#Models
def empleadosData(request):
    empleados = Empleados.objects.all()
    data = {'Empleados' : empleados}
    return render(request, 'templateCrudEmpleado/empleados-models.html', data)