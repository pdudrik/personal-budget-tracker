from django.urls import path
from . import views


app_name = "budget"


urlpatterns = [
    path("expenses/", views.ExpenseListView.as_view(), name="expense-list"),
    path("expense/add/", views.ExpenseAddView.as_view(), name="expense-add"),
    path("expense/<pk>/update/", views.ExpenseUpdateView.as_view(), name="expense-update"),
    path("expense/<pk>/delete/", views.ExpenseDeleteView.as_view(), name="expense-delete"),
    # path("expense/category/", views.ExpenseCategoryListView.as_view(), name="category-list"),
    # path("expense/category/add/", views.ExpenseCategoryAddView.as_view(), name="category-add"),
    # path("expense/category/<pk>/update/", views.ExpenseCategoryUpdateView.as_view(), name="category-update"),
    path("expense/category/delete/", views.ExpenseCategoryDeleteView.as_view(), name="expense-category-delete"),
    # path("expense/subcategory/", views.SubExpenseCategoryListView.as_view(), name="subcategory-list"),
    # path("expense/subcategory/add/", views.SubExpenseCategoryAddView.as_view(), name="subcategory-add"),
    # path("expense/subcategory/<pk>/update/", views.SubExpenseCategoryUpdateView.as_view(), name="subcategory-update"),
    # path("expense/subcategory/<pk>/delete/", views.ExpenseSubcategoryDeleteView.as_view(), name="expense-subcategory-delete"),
    path("income/", views.IncomeListView.as_view(), name="income-list"),
    path("income/add/", views.IncomeAddView.as_view(), name="income-add"),
    path("income/<pk>/update/", views.IncomeUpdateView.as_view(), name="income-update"),
    path("income/<pk>/delete/", views.IncomeDeleteView.as_view(), name="income-delete"),
    path("income/source/", views.IncomeSourceListView.as_view(), name="income-source-list"),
    path("settings/", views.SettingsView.as_view(), name="settings"),
    # path("income/source/add/", views.SourceAddView.as_view(), name="source-add"),
    # path("income/source/<pk>/update/", views.SourceUpdateView.as_view(), name="source-update"),
    # path("income/source/<pk>/delete/", views.SourceDeleteView.as_view(), name="source-delete"),
]
