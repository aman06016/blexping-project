from django.shortcuts import render,redirect
from .models import Blog
# Create your views here.
def create(request):
    if(request.method=='POST'):
        b=Blog()
        b.title=request.POST['title']
        b.body=request.POST['body']
        b.date=request.POST['date']
        print(request.user,"iloveu")
        b.author=request.user
        b.save()
        return redirect('home')
    else:
        return render(request,'blog/create.html')

def delete(request):
    return render(request,'blog/delete.html')
