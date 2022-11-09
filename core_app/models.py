from distutils.command.upload import upload
from pydoc import describe
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRegistrations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    dob = models.DateField(auto_now_add=True)

class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    describtion = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", null=True)
    date_created = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvote = models.ManyToManyField(User, related_name="upvote")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.answer

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Answers = models.ForeignKey(Answers, on_delete=models.CASCADE)

class Comments(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)






    
    

