from django.db import models

# Create your models here.

class Student(models.Model):
    """fields are: name, email, age, address"""
    name  = models.CharField(max_length=100)
    email =  models.EmailField(unique=True)
    age   = models.PositiveIntegerField()
    address = models.TextField()

    def __str__(self):
        return f'name: {self.name} email: {self.email} age: {self.age} and address: {self.address} '