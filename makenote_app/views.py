from django.shortcuts import render,redirect
from .models import User   
from django.contrib.auth import authenticate, login,user,         logout

# def login(request):
#     if request.method == "POST":
#         try:
#             user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
#             return render(request,'create.html')
#         except:
#             return render(request,'error.html')
#     return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        User.objects.create(
            username=request.POST['username'],
            password=request.POST['password'])
        return render(request,'success.html')

    return render(request,'register.html')

def login(request):
    # username = request.POST["username"]
    # password = request.POST["password"]
    user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'create.html')
    else:
        return render(request,'error.html')

def home(request):
    return render(request,'home.html')

def create(request):
    return render(request,'create.html')

def success(request):
    return render(request,'success.html')

def error(request):
    return render(request,'error.html')



