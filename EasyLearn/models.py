from django.db import models
from django import forms

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
    
# class Category(models.Model):
#     CHOICES = (
#         ('option1', 'Option 1'),
#         ('option2', 'Option 2'),
#         ('option3', 'Option 3'),
#     )
#     my_choice_field = forms.ChoiceField(choices=CHOICES)