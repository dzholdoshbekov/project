from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.name
    
# class User(AbstractUser):
#     tel = models.CharField("Телефон", max_length=15, blank=True, null=True)

#     REQUIRED_FIELDS = ['first_name', "last_name", "tel"]

#     def __str__(self):
#         return self.username
