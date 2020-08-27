from django.shortcuts import render,redirect
from .models import Blog,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
@login_required
def create_blog(request):
    if(request.method=='POST'):

        if(request.POST['title'])and(request.POST['body']):
            b=Blog()
            b.title=request.POST['title']
            b.body=request.POST['body']

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
    comments=Comment.objects.filter(post=blog,parent=None)
    replies=Comment.objects.filter(post=blog).exclude(parent=None)

    repList={}
    for rep in replies:
        if(rep.parent.id in repList.keys()):
            repList[rep.parent.id].append(rep)
        else:
            repList[rep.parent.id]=[rep]
    #print(repList)

    return render(request, 'blog/blogdetail.html',{'blog' : blog,'comments':comments ,'repList':repList})

@login_required
def upvote(request, blogid):

    blog=Blog.objects.get(pk=blogid)
    blog.likes+=1
    blog.save()

    comments=Comment.objects.filter(post=blog,parent=None)
    replies=Comment.objects.filter(post=blog).exclude(parent=None)

    repList={}
    for rep in replies:
        if(rep.parent.id in repList.keys()):
            repList[rep.parent.id].append(rep)
        else:
            repList[rep.parent.id]=[rep]
    #print(repList)


    return render(request, 'blog/blogdetail.html',{'blog' : blog,'comments':comments ,'repList':repList})

def profileblog(request,blogid):

    blog=Blog.objects.get(pk=blogid)
    user=User.objects.get(username=blog.author)
    allblog=Blog.objects.filter(author=user)
    return render(request,'blog/profile.html',{'userr':user,'blogs':allblog})

def profileuser(request,userid):

    user=User.objects.get(pk=userid)
    allblog=Blog.objects.filter(author=user)
    return render(request,'blog/profile.html',{'userr':user,'blogs':allblog})

def delete_blog(request,blogid):
    blog=Blog.objects.get(pk=blogid)
    user=User.objects.get(username=blog.author)

    blog=Blog.objects.get(pk=blogid)
    blog.delete()

    allblog=Blog.objects.filter(author=user)
    return render(request,'blog/profile.html',{'userr':user,'blogs':allblog})

def delete_account(request,accid):
    user=User.objects.get(pk=accid)
    user.delete()
    return redirect('home')

@login_required
def make_comment1(request,blogid):
    #print('gupta')
    #print('gupta' , blogid)

    #print('aman',comment.id)
    blog=Blog.objects.get(pk=blogid)
    #commentobj=Comment.objects.get(pk=commentid)
    obj=Comment()
    obj.body=request.POST['comment']
    obj.writer=request.user
    obj.post=blog

    obj.save()
    #comments=Comment.objects.filter(post=blog)
    #return render(request, 'blog/blogdetail.html',{'blog' : blog,'comments':comments })
    comments=Comment.objects.filter(post=blog,parent=None)
    replies=Comment.objects.filter(post=blog).exclude(parent=None)

    repList={}
    for rep in replies:
        if(rep.parent.id in repList.keys()):
            repList[rep.parent.id].append(rep)
        else:
            repList[rep.parent.id]=[rep]
    #print(repList)


    return render(request, 'blog/blogdetail.html',{'blog' : blog,'comments':comments ,'repList':repList})

@login_required
def make_comment2(request,blogid,commentid):
    #print('aman')
    #print('aman' , blogid)
    #print('aman',commentid)
    blog=Blog.objects.get(pk=blogid)
    commentobj=Comment.objects.get(pk=commentid)
    obj=Comment()
    obj.body=request.POST['comment']
    obj.writer=request.user
    obj.post=blog
    obj.parent=commentobj
    obj.save()
    #comments=Comment.objects.filter(post=blog)
    #return render(request, 'blog/blogdetail.html',{'blog' : blog,'comments':comments })

    comments=Comment.objects.filter(post=blog,parent=None)
    replies=Comment.objects.filter(post=blog).exclude(parent=None)

    repList={}
    for rep in replies:
        if(rep.parent.id in repList.keys()):
            repList[rep.parent.id].append(rep)
        else:
            repList[rep.parent.id]=[rep]
    #print(repList)


    return render(request, 'blog/blogdetail.html',{'blog' : blog,'comments':comments ,'repList':repList})

@login_required
def make_comment3(request,blogid,commentid,repid):
    #print('aman')
    #print('aman' , blogid)
    #print('aman',commentid)
    blog=Blog.objects.get(pk=blogid)
    commentobj=Comment.objects.get(pk=commentid)
    toMention= Comment.objects.get(pk=repid)
    obj=Comment()
    obj.body=request.POST['comment']
    obj.writer=request.user
    obj.post=blog
    obj.parent=commentobj
    obj.mention=toMention

    obj.save()
    #comments=Comment.objects.filter(post=blog)
    #return render(request, 'blog/blogdetail.html',{'blog' : blog,'comments':comments })

    comments=Comment.objects.filter(post=blog,parent=None)
    replies=Comment.objects.filter(post=blog).exclude(parent=None)

    repList={}
    for rep in replies:
        if(rep.parent.id in repList.keys()):
            repList[rep.parent.id].append(rep)
        else:
            repList[rep.parent.id]=[rep]
    #print(repList)

    return render(request, 'blog/blogdetail.html', {'blog' : blog,'comments':comments ,'repList':repList})

def deleteComment(request, commentid):

    obj=Comment.objects.get(pk=commentid)
    blog=obj.post
    obj.delete()

    comments=Comment.objects.filter(post=blog,parent=None)
    replies=Comment.objects.filter(post=blog).exclude(parent=None)

    repList={}
    for rep in replies:
        if(rep.parent.id in repList.keys()):
            repList[rep.parent.id].append(rep)
        else:
            repList[rep.parent.id]=[rep]
    #print(repList)


    return render(request, 'blog/blogdetail.html',{'blog' : blog,'comments':comments ,'repList':repList})
