from http import client
from django.contrib import admin
from .models import Client, PaymentMethod, Sale
# Register your models here.

admin.site.register(PaymentMethod)
admin.site.register(Sale)


