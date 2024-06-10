from django.db import models

# Create your models here.

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    email = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    