from django.shortcuts import render, redirect
from .models import InvestmentAccount
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # نحاول نجيب الحساب، ولو ما لقيناه ننشئه
    account, created = InvestmentAccount.objects.get_or_create(user=request.user)

    context = {
        'account': account,
        'created': created
    }
    return render(request, 'dashboard.html', context)
