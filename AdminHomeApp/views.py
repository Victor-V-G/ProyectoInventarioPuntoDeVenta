from django.shortcuts import render

# Create your views here.
def renderAdminHome(request):
    return render(request, 'templateAdminHome/adminhome.html')


