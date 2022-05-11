from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','first_name','address_street','phone','address_zipcode','address_city','address_country','bank_account_no','bank_name','email']
