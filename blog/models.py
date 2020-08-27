from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField(default=now)
    body=models.TextField(max_length=50000)
    likes=models.IntegerField(default=0)

    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    body=models.TextField(max_length=200)
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(default=now)
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)
    parent=models.ForeignKey('self',null=True,blank=True, on_delete=models.CASCADE, related_name='for_parents')
    mention=models.ForeignKey('self',null=True,blank=True, on_delete=models.CASCADE, related_name='for_mention')

    def __str__(self):
        return (self.body[:10] + '.... by ' + str(self.writer))
