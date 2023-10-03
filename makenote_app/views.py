from django.shortcuts import render,redirect
from .models import Person   
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.models import User

# def login(request):
#     if request.method == "POST":
#         try:
#             user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
#             return render(request,'create.html')
#         except:
#             return render(request,'error.html')
#     return render(request,'login.html')

# def register(request):

#     if request.method == 'POST':
#         Person.objects.create(
#             username=request.POST['username'],
#             password=request.POST['password'])
#         return render(request,'success.html')

#     return render(request,'register.html')

def register(request):

    if request.method == 'POST':
        user = User.objects.create(username=request.POST['username'])
        user.set_password(request.POST['password'])
        user.save()
        return render(request,'success.html')

    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user) 
            
    
        if user is not None:
            login_user(request, user)
            return render(request,'create.html')
        
        else:
            return render(request,'error.html')
        
    else:
        return render(request, 'login1.html')


# def login(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     # user = authenticate(request, username=username, password=password)
#     try:
#         user = authenticate(request, username=username, password=password)
#         login(request, user)
#         return render(request,'create.html')
        
#     except:
#         return render(request,'error.html')
    



     
def home(request):
    return render(request,'home.html')

def create(request):
    return render(request,'create.html')

def success(request):
    return render(request,'success.html')

def error(request):
    return render(request,'error.html')



