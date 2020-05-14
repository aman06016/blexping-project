from django.urls import path
from . import views

urlpatterns = [

    path('create/',views.create, name='create_blog'),
    path('delete/',views.delete, name='delete_blog'),
    

]
