from django import forms
from clients.models import Client

class ClientForm(forms.ModelForm):

    # Using meta class to link with our desired model, and the
    # fields we would like to be able to edit

    class Meta():
        
        model = Client
        fields = ('first_name','last_name','personal_id', 'email')