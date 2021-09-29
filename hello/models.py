from django.db import models

# Create your models here.
class HelloWorld(models.Model):  
    status = models.BooleanField(default=True)  # models.CharField(max_length=1024)
    value = models.TextField()
    active =  models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)