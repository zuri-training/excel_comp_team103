from django.shortcuts import render

# Create your views here.
def unauth(request):
    return render(request, "demo.html")

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        print(uploaded_file.name)
    return render(request, 'demo.html')