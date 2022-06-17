from django.db import models

# Create your models here.

class TODOIList(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)    
    Description = models.CharField(max_length=2000)

class Login(models.Model):
    FirstName = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    Email = models.CharField(primary_key=True,max_length=500)
    IsActive = models.CharField(max_length=500)
    Roles = models.CharField(max_length=500)
    Password = models.CharField(max_length=1000)
    Salt = models.CharField(max_length=1000)