from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Category, Account, Transaction, Budget
from .forms import CategoryForm, AccountForm, TransactionForm, BudgetForm

# Create your views here

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoryForm()
    return render(request, 'your_app/create_category.html', {'form': form})

@login_required
def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'your_app/update_category.html', {'form': form})

@login_required
def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'your_app/list_categories.html', {'categories': categories})

@login_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'your_app/category_detail.html', {'category': category})

@login_required
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('list_accounts')
    else:
        form = AccountForm()
    return render(request, 'your_app/create_account.html', {'form': form})

@login_required
def update_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('list_accounts')
    else:
        form = AccountForm(instance=account)
    return render(request, 'your_app/update_account.html', {'form': form})

@login_required
def list_accounts(request):
    accounts = Account.objects.filter(user=request.user)
    return render(request, 'your_app/list_accounts.html', {'accounts': accounts})

@login_required
def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'your_app/account_detail.html', {'account': account})

@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('list_transactions')
    else:
        form = TransactionForm()
    return render(request, 'your_app/create_transaction.html', {'form': form})

@login_required
def update_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('list_transactions')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'your_app/update_transaction.html', {'form': form})

@login_required
def list_transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'your_app/list_transactions.html', {'transactions': transactions})

@login_required
def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'your_app/transaction_detail.html', {'transaction': transaction})

@login_required
def create_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('list_budgets')
    else:
        form = BudgetForm()
    return render(request, 'your_app/create_budget.html', {'form': form})

@login_required
def update_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('list_budgets')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'your_app/update_budget.html', {'form': form})

@login_required
def list_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'your_app/list_budgets.html', {'budgets': budgets})

@login_required
def budget_detail(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    return render(request, 'your_app/budget_detail.html', {'budget': budget})

@login_required
def dashboard_view(request):
    accounts = Account.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(user=request.user)
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'your_app/dashboard.html', {
        'accounts': accounts,
        'transactions': transactions,
        'budgets': budgets,
    })
