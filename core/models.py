from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from decimal import Decimal

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class IncomeSource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount} on {self.date}"

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(IncomeSource, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.source} - {self.amount} on {self.date}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    total_income = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    total_expense = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        self.total_income = sum(income.amount for income in Income.objects.filter(user=self.user, date__year=self.year, date__month=self.month))
        self.total_expense = sum(expense.amount for expense in Expense.objects.filter(user=self.user, date__year=self.year, date__month=self.month))
        self.balance = self.total_income - self.total_expense
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Budget for {self.month}/{self.year}"

class FinancialReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_generated = models.DateField(auto_now_add=True)
    report_file = models.FileField(upload_to='reports/')

    def __str__(self):
        return f"Report generated on {self.date_generated}"
