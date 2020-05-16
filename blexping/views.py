from django.shortcuts import render

from django.http import HttpResponse as ht
from blog.models import Blog
import operator
def home(request):
    blogs=Blog.objects.all()
    d={}
    for x in blogs:
        d[x]=x.likes
    dick=dict(sorted(d.items(), key=operator.itemgetter(1)))
    b=list(dick.keys())
    bb=b[::-1]


    return render(request, 'home.html',{'blogs':bb})
