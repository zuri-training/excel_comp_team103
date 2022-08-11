from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")