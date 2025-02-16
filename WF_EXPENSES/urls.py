from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ExpenseViewSet, RecurringExpenseViewSet, BudgetViewSet, IncomeViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'recurring', RecurringExpenseViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'incomes', IncomeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
