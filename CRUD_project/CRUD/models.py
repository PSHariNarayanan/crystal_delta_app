from django.db import models

# Create your models here.
class User(models.Model) :
    username = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    password = models.CharField(max_length=225)

class Project(models.Model) :
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
