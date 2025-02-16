from rest_framework import serializers
from .models import Category, Expense, RecurringExpense, Budget, Income

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'subcategories']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'user', 'description', 'amount', 'currency', 'category', 'date', 'payment_method', 'receipt', 'notes', 'created_at']
        read_only_fields = ['user', 'created_at']

class RecurringExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringExpense
        fields = ['id', 'expense', 'frequency', 'start_date', 'end_date']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'category', 'amount', 'month', 'year']
        read_only_fields = ['user']

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'user', 'description', 'amount', 'currency', 'category', 'date', 'created_at']
        read_only_fields = ['user', 'created_at']
