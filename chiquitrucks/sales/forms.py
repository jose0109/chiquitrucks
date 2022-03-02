from django import forms
from sales.models import Sale,PaymentMethod

class SaleForm(forms.ModelForm):

    # Using meta class to link with our desired model, and the
    # fields we would like to be able to edit

    class Meta():
        
        model = Sale
        fields = ('client','amount','payment_method')

class PmForm(forms.ModelForm):

    class Meta():
        
        model = PaymentMethod
        fields = ('name','currency',)


# class CommentForm(forms.ModelForm):

#     class Meta():
        
#         model = Comment
#         fields = ('author','text')

#         widgets = {
#             'author':forms.TextInput(attrs={'class':'texinputclass'}),
#             'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
#         }