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
# from .errors import InsufficientFunds

@login_required
def index(request):
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('bank:staff_dashboard'))
    else:
        return HttpResponseRedirect(reverse('bank:dashboard'))

@login_required
def dashboard(request):
    assert not request.user.is_staff, 'Staff user routing customer view.'

    accounts = request.user.customer.accounts
    context = {
        'accounts': accounts,
    }
    return render(request, 'bank/dashboard.html', context)