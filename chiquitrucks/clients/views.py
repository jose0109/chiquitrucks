from django.shortcuts import render
from .forms import ClientForm
from .models import Client
from django.urls import reverse_lazy

from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView)



# Create your views here.

class ClientListView(ListView):
    model = Client

    # Field Lookups - documentation
    # With get_queryset im doing basically a sql query on my model

    def get_queryset(self):
        return Client.objects.all()

class ClientDetailView(DetailView):
    model = Client

class CreateClientView(CreateView):
    
    # We need a way to make sure that the user has to be logged to create a post
    # when using function based views we used decorators but now we must use mixins -- LoginRequiredMixin,

    # login_url = '/login/'
    # redirect_field_name = 'clients/client_list.html'
    form_class = ClientForm
    model = Client

    # To update an existing post
class ClientUpdateView(UpdateView):

    # login_url = '/login/'
    redirect_field_name = 'clients/client_list.html'
    form_class = ClientForm
    model = Client

class ClientDeleteView(DeleteView):

    model = Client
    success_url = reverse_lazy('clients:client_list')