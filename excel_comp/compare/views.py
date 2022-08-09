from django.shortcuts import render

# Create your views here.
def unauth(request):
    return render(request, "demo.html")