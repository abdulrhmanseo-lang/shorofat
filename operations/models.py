from django.db import models
from investors.models import InvestmentAccount  # إذا عندك ربط بالمستثمرين

# ✅ هذا هو الموديل اللي كان ناقصك (Project)
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        InvestmentAccount, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name


# ✅ مثال موديل ثاني عندك
class Transaction(models.Model):
    account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.amount} ريال"
