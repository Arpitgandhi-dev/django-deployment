from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    portfolio_site = models.URLField(blank = True)

    profile_pic = models.ImageField(upload_to = 'profile_pic',  blank = False, default='SOME STRING')

   

    def __str__(self):
        return self.user.username

class Blogdata(models.Model):

    Name = models.CharField(max_length = 256)
    Blog = models.TextField()

    def __str__(self):
        return self.Name



