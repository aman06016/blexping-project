from django.urls import path
from . import views

urlpatterns = [

    path('create/',views.create, name='create_blog'),
    path('<int:blog_id>/',views.blogdetail, name='blogdetail'),
    path('upvote/<int:blogid>/', views.upvote,name='upvote'),
    path('profile/<int:blogid>/', views.profile,name='profile'),
    path('profileuser/<int:userid>/', views.profileuser,name='profileuser'),
    path('delete/<int:blogid>/',views.delete, name='delete_blog'),


]
