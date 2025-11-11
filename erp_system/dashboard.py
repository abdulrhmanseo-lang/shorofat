from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from accounts.models import User
from operations.models import Operation
from finance.models import Invoice

def dashboard(request):
    users_count = User.objects.count()
    ops_count = Operation.objects.count()
    invoices_count = Invoice.objects.count()
    return render(request, "admin/dashboard.html", {
        "users_count": users_count,
        "ops_count": ops_count,
        "invoices_count": invoices_count,
    })
