from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Fakultas(models.Model):
    fakul = models.CharField(max_length=50,unique=True)

    def __str__(self): return self.fakul


class Userdata(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    faculty = models.ForeignKey(Fakultas,on_delete=models.CASCADE,default= 1)
    is_voted = models.BooleanField(default=False)

    def __str__(self):return self.user.username


class Voting(models.Model):
    name = models.CharField(max_length=50)
    pic = models.CharField(max_length=50)
    text = models.TextField()
    voters = models.IntegerField()

    def __str__(self): return self.name


class Token(models.Model):
    token_id = models.CharField(max_length=40,unique=True)
    redeemed = models.BooleanField(default=False)

    def __str__(self): return self.token_id
