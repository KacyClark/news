from django.contrib.auth.models import AbstractUser
from django.db import models



class Role(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=256)
    decription = models.TextField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )