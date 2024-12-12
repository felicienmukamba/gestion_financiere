from django.contrib import admin
from .models import Besoin, Category, Account, EtatBesoin, Transaction, Budget

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'initial_balance', 'current_balance', 'created_at', 'updated_at')
    search_fields = ('user__username', 'name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('user', 'name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'account', 'category', 'transaction_type', 'amount', 'created_at', 'updated_at')
    search_fields = ('user__username', 'account__name', 'category__name', 'transaction_type', 'amount')
    list_filter = ('transaction_type', 'created_at', 'updated_at')
    ordering = ('created_at',)
    raw_id_fields = ('user', 'account', 'category')

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'account', 'category', 'amount', 'start_date', 'end_date', 'spent_amount', 'created_at', 'updated_at')
    search_fields = ('user__username', 'account__name', 'category__name', 'amount')
    list_filter = ('start_date', 'end_date', 'created_at', 'updated_at')
    ordering = ('start_date',)
    raw_id_fields = ('user', 'account', 'category')

admin.site.register(Besoin)
admin.site.register(EtatBesoin)