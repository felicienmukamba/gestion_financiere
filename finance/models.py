from django.db import models
from django.contrib.auth import get_user_model

from section.models import Beneficiere, Etudiant

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='accounts')
    name = models.CharField(max_length=255)
    initial_balance = models.DecimalField(max_digits=12, decimal_places=2)
    current_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

    def save(self, *args, **kwargs):
        # Initialize current balance with initial balance when account is first created
        if not self.pk:
            self.current_balance = self.initial_balance
        super().save(*args, **kwargs)

class Transaction(models.Model):
    INCOME = 'entree'
    EXPENSE = 'sortie'
    TRANSACTION_TYPES = [
        (INCOME, 'entree'),
        (EXPENSE, 'sortie'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='transactions')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='transactions')
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    source = models.ForeignKey(Etudiant, blank=True, null=True, on_delete=models.CASCADE)
    beneficiere = models.ForeignKey(Beneficiere, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()}: {self.amount} on {self.created_at} by {self.user.username}"
    


    def save(self, *args, **kwargs):
        # Adjust account balance based on transaction type
        if self.transaction_type == self.INCOME:
            self.account.current_balance += self.amount
        elif self.transaction_type == self.EXPENSE:
            self.account.current_balance -= self.amount
        self.account.save()
        super().save(*args, **kwargs)

class Budget(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='budgets')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='budgets')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='budgets')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    spent_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Budget: {self.amount} for {self.category.name} from {self.start_date} to {self.end_date}"

    def update_spent_amount(self):
        # Utilisation de 'created_at' au lieu de 'date'
        transactions = Transaction.objects.filter(
            user=self.user, account=self.account, category=self.category,
            created_at__gte=self.start_date, created_at__lte=self.end_date, transaction_type=Transaction.EXPENSE
        )
        self.spent_amount = sum(t.amount for t in transactions)

    def save(self, *args, **kwargs):
        self.update_spent_amount()
        super().save(*args, **kwargs)



class Besoin(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class EtatBesoin(models.Model):
    motif = models.CharField(max_length=255)
    description = models.TextField()
    besoin = models.ManyToManyField(Besoin)
    created = models.DateTimeField(auto_now_add=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.motif