from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Category, Account, Transaction, Budget
from .forms import CategoryForm, AccountForm, TransactionForm, BudgetForm
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = reverse_lazy('account-list')

class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('transaction-list')

class BudgetDeleteView(LoginRequiredMixin, DeleteView):
    model = Budget
    success_url = reverse_lazy('budget-list')

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        accounts = Account.objects.filter(user=request.user)
        transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')[:10]
        budgets = Budget.objects.filter(user=request.user)
        context = {
            'accounts': accounts,
            'transactions': transactions,
            'budgets': budgets,
        }
        return render(request, 'app/dashboard.html', context)

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'app/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'app/category_detail.html'
    context_object_name = 'category'

class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'app/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'app/account_form.html'
    success_url = reverse_lazy('account-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'app/account_form.html'
    success_url = reverse_lazy('account-list')

class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'app/account_detail.html'
    context_object_name = 'account'

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'app/transaction_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'app/transaction_form.html'
    success_url = reverse_lazy('transaction-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'app/transaction_form.html'
    success_url = reverse_lazy('transaction-list')

class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'app/transaction_detail.html'
    context_object_name = 'transaction'

class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'app/budget_list.html'
    context_object_name = 'budgets'

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'app/budget_form.html'
    success_url = reverse_lazy('budget-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BudgetUpdateView(LoginRequiredMixin, UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'app/budget_form.html'
    success_url = reverse_lazy('budget-list')

class BudgetDetailView(LoginRequiredMixin, DetailView):
    model = Budget
    template_name = 'app/budget_detail.html'
    context_object_name = 'budget'