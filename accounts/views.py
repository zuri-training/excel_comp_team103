from django.shortcuts import render, redirect
from .forms import RegForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def registerPage(request):
    
    form = RegForm()


    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Account created successfully")
            return redirect('/account/login')


    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.info(request, "username or password is incorrect") 
               

    context ={}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/account/login')    


def error_404_view(request,exception):
    return render(request, 'not-found.html')

    