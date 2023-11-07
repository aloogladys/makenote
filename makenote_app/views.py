from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.models import User
from .models import Note

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
        messages.success(request, 'You have succesfully registered')
        # return render(request,'success.html')

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
            return redirect('list_notes')
        
        else:
            return render(request,'error.html')
        
    else:
        return render(request, 'login1.html')



    



def home(request):
    return render(request,'home.html')

def create(request):
    if request.user.is_authenticated == True:
        pass
    else:
        return redirect('login')
    
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        user = request.user
        Note.objects.create(title = title, description = description, user = user )
        return redirect('list_notes')

    return render(request,'create.html')


def list_notes(request):
    if request.user.is_authenticated == True:
        pass 
    else:
        return redirect('login')
    
    # pull all notes from the database 

    note_queryset = Note.objects.filter(user = request.user )
    context = {"note_queryset":note_queryset}

    return render(request, 'list_notes.html', context )


def delete_note(request, id):
    try:
        note = Note.objects.get(id = id)
        note.delete()
    except:
        pass
    return redirect('list_notes')


def update_note(request, id):
    note = Note.objects.get(id = id)

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        # update the note
        note.title = title
        note.description = description
        note.save()
        return redirect('list_notes')
        

    context = {'note':note}
    return render(request, 'update_note.html', context)

def person (request):
    return render (request, 'person.html')
    


















def success(request):
    return render(request,'success.html')

def error(request):
    return render(request,'error.html')



