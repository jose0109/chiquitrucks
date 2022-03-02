from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from . import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.CustomUserCreationForm
    # Reverse lazy allows to return login page after signing up.
    # using only reverse would not really allow the signup before redirecting
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def Profile(request):
    return render(request, 'users/profile.html')

    