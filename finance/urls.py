from django.urls import path
from .views import (
    AccountDeleteView, BudgetDeleteView, DashboardView, CategoryListView, CategoryCreateView, CategoryUpdateView, 
    CategoryDetailView, AccountListView, AccountCreateView, AccountUpdateView, 
    AccountDetailView, TransactionDeleteView, TransactionListView, TransactionCreateView, 
    TransactionUpdateView, TransactionDetailView, BudgetListView, 
    BudgetCreateView, BudgetUpdateView, BudgetDetailView
)

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('accounts/add/', AccountCreateView.as_view(), name='account-add'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('accounts/<int:pk>/edit/', AccountUpdateView.as_view(), name='account-edit'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/add/', TransactionCreateView.as_view(), name='transaction-add'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction-edit'),
    path('budgets/', BudgetListView.as_view(), name='budget-list'),
    path('budgets/add/', BudgetCreateView.as_view(), name='budget-add'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
    path('budgets/<int:pk>/edit/', BudgetUpdateView.as_view(), name='budget-edit'),

    
    path('accounts/<int:pk>/delete/', AccountDeleteView.as_view(), name='account-delete'),
    path('transactions/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('budgets/<int:pk>/delete/', BudgetDeleteView.as_view(), name='budget-delete'),
]
