from django.shortcuts import render,redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def create(request):
    if(request.method=='POST'):

        if(request.POST['title'])and(request.POST['body'])and(request.POST['date']):
            b=Blog()
            b.title=request.POST['title']
            b.body=request.POST['body']
            b.date=request.POST['date']
            #print(request.user,"iloveu")
            b.author=request.user
            b.save()
            address='/blog/profile/'
            address+= str(b.id)
            address+='/'
            return redirect(address)
        else:
            return render(request,'blog/create.html',{'error': ' you must fill all of the form'})

    else:
        return render(request,'blog/create.html')



def blogdetail(request, blog_id):
    blog=Blog.objects.get(pk=blog_id)
    return render(request, 'blog/blogdetail.html',{'blog' : blog })

@login_required
def upvote(request, blogid):

    blog=Blog.objects.get(pk=blogid)

    blog.likes+=1

    blog.save()
    return render(request,'blog/blogdetail.html',{'blog' : blog })

def profile(request,blogid):

    blog=Blog.objects.get(pk=blogid)
    user=User.objects.get(username=blog.author)
    allblog=Blog.objects.filter(author=user)
    return render(request,'blog/profile.html',{'userr':user,'blogs':allblog})

def profileuser(request,userid):

    user=User.objects.get(pk=userid)
    allblog=Blog.objects.filter(author=user)
    return render(request,'blog/profile.html',{'userr':user,'blogs':allblog})

def delete(request,blogid):
    blog=Blog.objects.get(pk=blogid)
    user=User.objects.get(username=blog.author)

    blog=Blog.objects.get(pk=blogid)
    blog.delete()

    allblog=Blog.objects.filter(author=user)
    return render(request,'blog/profile.html',{'userr':user,'blogs':allblog})
