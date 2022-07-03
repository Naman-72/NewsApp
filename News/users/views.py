from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def signin(request):
    if request.method == "POST":
        user1 = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(username=user1,password=pass1)
        if user is not None :
            login(request,user)
            n1 = user.get_username()
            return render(request,"home.html",{"us":n1})
        else :
            messages.error(request,"Wrong Credentials")
            return render(request, "login.html")
    return render(request, "login.html")



def signup(request):
    if request.method == "POST":
        firstname = request.POST.get('fn')
        lastname = request.POST.get('ln')
        name = firstname+lastname
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_verify = request.POST.get('password2')
        email = request.POST.get('email')
        # if password != password_verify :
        #     return render(request,"signup.html")
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"User Created Successfully")
        return redirect('login')
    return render(request, "signup.html")

def signout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('india')
