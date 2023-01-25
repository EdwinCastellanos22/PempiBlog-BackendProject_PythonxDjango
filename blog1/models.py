from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default='profile.jpg')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    post_image= models.ImageField(default='post.png')
    title= models.CharField(max_length=50)
    text= models.TextField()
    time= models.DateTimeField(auto_now_add=True)
    likes= models.IntegerField(default=0)

    def __str__(self):
        return self.title