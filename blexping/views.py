from django.shortcuts import render

from django.http import HttpResponse as ht

def home(request):
    #return ht("home page")
    
    return render(request, 'home.html')
