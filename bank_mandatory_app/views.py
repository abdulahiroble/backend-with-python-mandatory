from decimal import Decimal
from secrets import token_urlsafe
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.core.exceptions import PermissionDenied
# from django.db import IntegrityError
# from .forms import TransferForm, UserForm, CustomerForm, NewUserForm, NewAccountForm
from .models import Account, Customer
from .errors import InsufficientFunds

@login_required
def index(request):
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('bank_mandatory_app:staff_dashboard'))
    else:
        return HttpResponseRedirect(reverse('bank_mandatory_app:dashboard'))

@login_required
def dashboard(request):
    assert not request.user.is_staff, 'Staff user routing customer view.'

    accounts = request.user.customer.accounts
    context = {
        'accounts': accounts,
    }
    return render(request, 'bank_mandatory_app/dashboard.html', context)

@login_required
def account_details(request, pk):
    assert not request.user.is_staff, 'Staff user routing customer view.'
 
    account = get_object_or_404(Account, user=request.user, pk=pk)
    context = {
        'account': account,
    }
    return render(request, 'bank_mandatory_app/account_details.html', context)


# Staff views

@login_required
def staff_dashboard(request):
    assert request.user.is_staff, 'Customer user routing staff view.'

    return render(request, 'bank/staff_dashboard.html')

@login_required
def staff_search_partial(request):
    assert request.user.is_staff, 'Customer user routing staff view.'

    search_term = request.POST['search_term']
    customers = Customer.search(search_term)
    context = {
        'customers': customers,
    }
    return render(request, 'bank/staff_search_partial.html', context)
