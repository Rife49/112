from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# Relational Databases --> Tables
class Post(models.Model):
    title = models.CharField(max_length=128) # string
    subtitle = models.CharField(max_length=128) # string
    body = models.TextField() # string
    created_on = models.DateTimeField(auto_now_add=True) # Date, datetime
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        ) # string / object
    
    def __str__(self): #toString method
        return f"{self.title} by {self.author}"