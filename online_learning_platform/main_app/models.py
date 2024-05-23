from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title
    

class Course(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title