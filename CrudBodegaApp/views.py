from django.shortcuts import render

# Create your views here.
def renderTemplateCrudBodega (request):
    return render(request, "templateCrudBodega/crudbodega.html")