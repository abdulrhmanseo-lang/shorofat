from django.db import models
from django.contrib.auth.models import User

class InvestmentAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_investments = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    monthly_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    last_action = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"محفظة {self.user.username}"

class Transaction(models.Model):
    account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE, related_name='investor_transactions')

    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50)  # إيداع / سحب / استثمار / ربح
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.type} - {self.amount} ريال"
