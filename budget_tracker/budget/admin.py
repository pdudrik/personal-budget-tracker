from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ExpenseCategory)
admin.site.register(ExpenseSubcategory)
admin.site.register(ExpenseRecord)
admin.site.register(IncomeSource)
admin.site.register(IncomeRecord)