from django.shortcuts import render
from .models import User   

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request,'create.html')
        except:
            return render(request,'error.html')
    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        User.objects.create(
            username=request.POST['username'],
            password=request.POST['password'])
        return render(request,'success.html')

    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def create(request):
    return render(request,'create.html')

def success(request):
    return render(request,'success.html')

def error(request):
    return render(request,'error.html')



