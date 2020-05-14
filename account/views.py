from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse as ht

# Create your views here.
def signup(request):
    if(request.method=='POST'):
        try:
            obj=User.objects.get(username=request.POST['username'])

            return render(request,'account/signup.html',{'error':'username already exist!!!'})
        except User.DoesNotExist:

            if(request.POST['password1'] != request.POST['password2']):
                return render(request,'account/signup.html',{'error':'password do not match'})
            else:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password2'])
                user.save()
                auth.login(request,user)
                return redirect('home')

    else:
        return render(request,'account/signup.html')



def login(request):
    if(request.method=='POST'):

        user=auth.authenticate(username=request.POST['username'] ,password=request.POST['password'])
        if(user is None):

            return render(request,'account/login.html' ,{'error':'wrong username or password'})

        else:
            auth.login(request,user)
            return redirect('home')

    else:
        return render(request,'account/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'home.html')
