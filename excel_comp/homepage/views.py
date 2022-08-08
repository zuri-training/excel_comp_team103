from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "home.html")

def page_not_found(request):
    return render(request, "not-found.html")