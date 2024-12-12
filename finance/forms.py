from django import forms
from .models import Besoin, Category, Account, EtatBesoin, Transaction, Budget


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
    

    def clean(self):
        return super().clean()

    class Meta:
        model = Transaction
        fields = ['account', 'category', 'transaction_type',
                  'source', 'beneficiere', 'amount', 'description']


class BudgetForm(BootstrapFormMixin, forms.ModelForm):
    start_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Budget
        fields = ['account', 'category', 'amount', 'start_date', 'end_date']



class BesoinForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Besoin
        fields = ['name', 'description']


class EtatBesoinForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = EtatBesoin
        fields = ["motif", "description", "besoin", "budget"]
