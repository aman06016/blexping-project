from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=False, auto_now_add=False)
    body=models.TextField(max_length=50000)
    likes=models.IntegerField(default=0)

    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
