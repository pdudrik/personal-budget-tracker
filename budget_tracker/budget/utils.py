from .models import ExpenseCategory, IncomeRecord, ExpenseRecord, Goal
from django.db.models import Sum

def valid_int_id(value):
    try:
        num = int(value)
    except (ValueError, TypeError):
        return None
    
    if num > 0:
        return num
    return None


def get_categories_json():
    data = {}
    for category in ExpenseCategory.objects.prefetch_related("subcategories").all():
        data[str(category.id)] = []
        
        for subcategory in category.subcategories.all():
            data[str(category.id)].append({
                "id": str(subcategory.id),
                "name": subcategory.name,
            })
    
    return data


# def get_goal_balance(pk):
#     goal = None
#     balance = None
    
#     try:
#         goal = Goal.objects.get(pk=pk)
#     except Goal.DoesNotExist:
#         print(f"Goal with ID={pk} does not exist")
#         return None

#     expense_list = goal.expenses.all()
#     income_list = goal.incomes.all()

#     for expense in expense_list:
#         if balance is None:
#             balance = -expense.value
#             continue
        
#         balance -= expense.value

#     for income in income_list:
#         if balance is None:
#             balance = abs(expense.value)
#             continue

#         balance += abs(income.value)

#     return balance


def get_goal_balance(pk):
    try:
        goal = Goal.objects.get(pk=pk)

    except Goal.DoesNotExist:
        return None
    
    expense_total = goal.expenses.aggregate(total=Sum("value"))["total"] or 0

    return round(expense_total, 2)