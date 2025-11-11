from django.db import models
from operations.models import Project

class Invoice(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"فاتورة {self.id} - {self.project.name}"
