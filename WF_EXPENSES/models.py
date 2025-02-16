from django.db import models
from django.contrib.auth.models import User

# Choices for currencies, payment methods, and recurrence frequencies
CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound'),
]

PAYMENT_METHOD_CHOICES = [
    ('CASH', 'Cash'),
    ('CREDIT', 'Credit Card'),
    ('DEBIT', 'Debit Card'),
    ('BANK', 'Bank Transfer'),
]

FREQUENCY_CHOICES = [
    ('DAILY', 'Daily'),
    ('WEEKLY', 'Weekly'),
    ('BIWEEKLY', 'Bi-Weekly'),
    ('MONTHLY', 'Monthly'),
    ('YEARLY', 'Yearly'),
]

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    category = models.ForeignKey(Category, related_name='expenses', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount} {self.currency}"

class RecurringExpense(models.Model):
    expense = models.ForeignKey(Expense, related_name='recurrences', on_delete=models.CASCADE)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Recurring: {self.expense.description} ({self.frequency})"

class Budget(models.Model):
    user = models.ForeignKey(User, related_name='budgets', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='budgets', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.IntegerField()  # 1-12
    year = models.IntegerField()

    def __str__(self):
        return f"Budget for {self.category} - {self.amount} for {self.month}/{self.year}"

class Income(models.Model):
    user = models.ForeignKey(User, related_name='incomes', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    category = models.CharField(max_length=100, default="Income")
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount} {self.currency}"
