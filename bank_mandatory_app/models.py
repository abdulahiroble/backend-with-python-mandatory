from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.IntegerField()
    birth_date = models.DateField()
    group_type = models.IntegerField()
    accounts = models.ManyToManyField('Accounts', through='Customer')

class Account(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.IntegerField()
    
class Group(models.Model):
    type_id = models.IntegerField()
    name = models.CharField(max_length=100)
    
    
class Loans(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=3, decimal_places=2)