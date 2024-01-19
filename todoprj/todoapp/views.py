from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    if request.method=="POST":
        task=request.POST.get("task")
        new_todo=todo(user=request.user, todoname=task)
        new_todo.save()

    all_todos= todo.objects.filter(user=request.user)
    context={
        'todos':all_todos
    }
    return render(request,'todoapp/todo.html',context)

@login_required
def logoutview(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method =="POST":
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')

        if len(password)<3:
            messages.error(request,"password must be at least 3 character")
            return redirect('register')
        
        get_all_users=User.objects.filter(username=username)
        if get_all_users:
            messages.error(request,"username already exist")
            return redirect('register')
    
        


        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'user successfully created')
        return redirect('login')
    return render(request,'todoapp/register.html',{})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method=='POST':
        username=request.POST.get('uname')
        password= request.POST.get('pass')

        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('homepage')
        else:
            messages.error(request,'user does not exist')
            return redirect('login')
    return render(request,'todoapp/login.html',{})

@login_required
def deleteTask(request,name):
    get_task=todo.objects.filter(user=request.user,todoname=name)
    get_task.delete()

    return redirect("homepage")

@login_required
def updateTask(request,name):
    todo.objects.filter(user=request.user,todoname=name).update(status="True")
    return redirect("homepage")
    
    