from django.shortcuts import render

# Create your views here.
def renderCrudEmpleados(request):
    return render(request, 'templateCrudEmpleado/crudempleado.html')


def renderTemplateFormularioAgregarEmpleado(request):
    return render(request, 'templateCrudEmpleado/formularioempleado.html')

