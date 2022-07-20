from django.db import models

# Create your models here.
class User(models.Model):
    
    email = models.EmailField(unique=True, blank=False)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email