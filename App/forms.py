from .models import *
from django import forms
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'

