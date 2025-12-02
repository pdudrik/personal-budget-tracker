from django.urls import path
from . import views


app_name = "budget"


urlpatterns = [
    path("expenses/", views.ExpenseListView.as_view(), name="expense-list"),
    path("expense/add/", views.ExpenseAddView.as_view(), name="expense-add"),
    path("expense/<pk>/update/", views.ExpenseUpdateView.as_view(), name="expense-update"),
    path("expense/<pk>/delete/", views.ExpenseDeleteView.as_view(), name="expense-delete"),
    # path("expense/category/delete/", views.ExpenseCategoryDeleteView.as_view(), name="expense-category-delete"),
    path("income/", views.IncomeListView.as_view(), name="income-list"),
    path("income/add/", views.IncomeAddView.as_view(), name="income-add"),
    path("income/<pk>/update/", views.IncomeUpdateView.as_view(), name="income-update"),
    path("income/<pk>/delete/", views.IncomeDeleteView.as_view(), name="income-delete"),
    path("income/source/", views.IncomeSourceListView.as_view(), name="income-source-list"),
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path("", views.HomeView.as_view(), name="home")
]
