from django import forms
from .models import Category, Account, Transaction, Budget

class BootstrapFormMixin:
    """Mixin to add Bootstrap classes to form fields."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CategoryForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class AccountForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'initial_balance']

class TransactionForm(BootstrapFormMixin, forms.ModelForm):
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Transaction
        fields = ['account', 'category', 'transaction_type', 'amount', 'description', 'date']

class BudgetForm(BootstrapFormMixin, forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Budget
        fields = ['account', 'category', 'amount', 'start_date', 'end_date']
