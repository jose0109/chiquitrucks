from django.shortcuts import render
from django.utils import timezone
from .forms import SaleForm,PmForm
from .models import Sale, PaymentMethod
from django.urls import reverse_lazy

from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView)



# Create your views here.

class SaleListView(ListView):
    model = Sale

    # Field Lookups - documentation
    # With get_queryset im doing basically a sql query on my model

    def get_queryset(self):
        return Sale.objects.all()

class SaleDetailView(DetailView):
    model = Sale

class CreateSaleView(CreateView):
    
    # We need a way to make sure that the user has to be logged to create a post
    # when using function based views we used decorators but now we must use mixins -- LoginRequiredMixin,

    # login_url = '/login/'
    # redirect_field_name = 'sales/sale_list.html'
    form_class = SaleForm
    model = Sale

    # To update an existing post
class SaleUpdateView(UpdateView):

    # login_url = '/login/'
    redirect_field_name = 'sales/sale_list.html'
    form_class = SaleForm
    model = Sale

class SaleDeleteView(DeleteView):

    model = Sale
    success_url = reverse_lazy('sales_list')

# Payment Methods Views

class PmListView(ListView):
    model = PaymentMethod

    # Field Lookups - documentation
    # With get_queryset im doing basically a sql query on my model

    def get_queryset(self):
        return PaymentMethod.objects.all()

class PmCreateView(CreateView):
    
    # login_url = '/login/'

    form_class = PmForm
    model = PaymentMethod

class PmDeleteView(DeleteView):

    model = PaymentMethod
    success_url = reverse_lazy('sales:payment_methods')