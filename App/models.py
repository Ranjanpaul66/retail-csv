from django.db import models

class Customers(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    address_street = models.CharField(max_length=200, blank=True,)
    phone = models.CharField(max_length=25, blank=True,null=True)
    address_zipcode = models.CharField(max_length=10, blank=True,null=True)
    address_city = models.CharField(max_length=80, blank=True,null=True)
    address_country = models.CharField(max_length=80, blank=True,null=True)
    bank_account_no = models.CharField(max_length=50, blank=True,null=True)
    bank_name = models.CharField(max_length=200, blank=True,null=True)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.name
