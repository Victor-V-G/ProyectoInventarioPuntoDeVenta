from django.shortcuts import render

# Create your views here.
def renderTemplateHome (request):
    return render(request, "templateHome/home.html")