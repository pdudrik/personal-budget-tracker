from django.urls import path
from . import views


app_name = "budget"


urlpatterns = [
    path("expenses/", views.ExpenseListView.as_view(), name="expense-list"),
    path("expense/add/", views.ExpenseAddView.as_view(), name="expense-add"),
    path("expense/<pk>/update/", views.ExpenseUpdateView.as_view(), name="expense-update"),
    path("expense/<pk>/delete/", views.ExpenseDeleteView.as_view(), name="expense-delete"),
    path("income/", views.IncomeListView.as_view(), name="income-list"),
    path("income/add/", views.IncomeAddView.as_view(), name="income-add"),
    path("income/<pk>/update/", views.IncomeUpdateView.as_view(), name="income-update"),
    path("income/<pk>/delete/", views.IncomeDeleteView.as_view(), name="income-delete"),
    path("goals/", views.GoalListView.as_view(), name="goal-list"),
    path("goal/<pk>", views.GoalDetailView.as_view(), name="goal-detail"),
    path("goal/add/", views.GoalAddView.as_view(), name="goal-add"),
    path("goal/<pk>/update/", views.GoalUpdateView.as_view(), name="goal-update"),
    path("goal/<pk>/delete/", views.GoalDeleteView.as_view(), name="goal-delete"),
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path("", views.HomeView.as_view(), name="home")
]
