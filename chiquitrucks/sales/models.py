from django.db import models
from django.utils import timezone
from django.urls import reverse
from clients.models import Client

# Create your models here.

class PaymentMethod(models.Model):
    name = models.CharField(max_length=20)
    currency = models.CharField(max_length=3, default='')
   
    def __str__(self):
        return f'{self.name} {self.currency}'

    def get_absolute_url(self):
        return reverse('sales:payment_methods')
    

class Sale(models.Model):
    
    created = models.DateTimeField(default=timezone.now)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='transactions')
    amount = models.IntegerField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE, related_name='transaction')
    
    def __str__(self):
        return f'{self.created} - {self.pk}'

    # This is where im redirected after saving a new sale
    def get_absolute_url(self):
        return reverse('sales:sales_list')
    
    


