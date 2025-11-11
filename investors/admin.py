from django.contrib import admin
from .models import InvestmentAccount, Transaction

admin.site.register(InvestmentAccount)
admin.site.register(Transaction)
