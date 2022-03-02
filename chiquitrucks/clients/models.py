from django.db import models
from django.urls import reverse

# Create your models here.

class Client(models.Model):

    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    personal_id = models.IntegerField(unique=True, blank=False)
    email = models.EmailField(unique=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    # This is where im redirected after saving a new sale
    def get_absolute_url(self):
        return reverse('clients:client_list')