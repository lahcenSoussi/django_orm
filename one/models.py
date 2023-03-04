from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    label= models.CharField(max_length=100)
    #description = models.TextField(1)
    def __str__(self):
        return self.label
    
class Course(models.Model):
    label = models.CharField(max_length=100)
    price = models.FloatField()
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.label
     
class Prof(models.Model):
    full_name=models.CharField(max_length=100)
    age = models.IntegerField()
    CIN = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.full_name