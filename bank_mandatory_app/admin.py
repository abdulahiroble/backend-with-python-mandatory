from django.contrib import admin
from .models import Customer, Account, Employee, Group, Ledger

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Employee)
admin.site.register(Group)
admin.site.register(Ledger)

