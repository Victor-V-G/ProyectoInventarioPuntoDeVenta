from django.shortcuts import render

# Create your views here.
#RENDER PARA EL TEMPLATE DEL HOME
def renderTemplateHome (request):
    return render(request, "templateHome/home.html")