# Generated by Django 4.0.4 on 2022-05-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('address_street', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('address_zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('address_city', models.CharField(blank=True, max_length=80, null=True)),
                ('address_country', models.CharField(blank=True, max_length=80, null=True)),
                ('bank_account_no', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
