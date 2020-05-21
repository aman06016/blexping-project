from django.urls import path
from . import views

urlpatterns = [

    path('create/',views.create_blog, name='create_blog'),
    path('<int:blog_id>/',views.blogdetail, name='blogdetail'),
    path('upvote/<int:blogid>/', views.upvote,name='upvote'),
    path('profile/<int:blogid>/', views.profileblog,name='profile'),
    path('profileuser/<int:userid>/', views.profileuser,name='profileuser'),
    path('delete/<int:blogid>/',views.delete_blog, name='delete_blog'),
    path('deleteaccount/<int:accid>/', views.delete_account, name='delete_account'),

    path('newcomment/<int:blogid>/',views.make_commentt,name='make_commentt'),
    path('newcomment/<int:blogid>/<int:commentid>/',views.make_comment,name='make_comment')



]
