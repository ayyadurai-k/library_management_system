from django.db import models


"""
Book - Model
name -> field
CharField -> Field Type
Inside parentheses - attributes or constraints
"""


# Create your models here.
class Book(models.Model):
    name = models.CharField(
        max_length=30
    )  # Use char field when you want to specify tbe length
    description = (
        models.TextField()
    )  # Use text field when you dont want to specify tbe length
    
    def __str__(self):
        return self.name


# TO CONVERT MODEL INTO TABLE

#1. python manage.py makemigrations
#2.  python manage.py migrate

# CREATE , READ , UPDATE , DELETE => CRUD