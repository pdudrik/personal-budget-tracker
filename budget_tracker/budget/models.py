from datetime import datetime
from django.db import models


GOAL_STATUS_CHOICES = [
    ("in_progress", "In Progress"),
    ("completed", "Completed"),
]

DEFAULT_CURRENCY = "eur"
DEFAULT_GOAL_STATUS_CHOICE = GOAL_STATUS_CHOICES[0][0]


class Goal(models.Model):
    name = models.CharField(max_length=30)
    target_value = models.DecimalField(
        decimal_places=2,
        max_digits=7
    )
    currency = models.CharField(
        max_length=3,
        default="eur",
        blank=True
    )
    created = models.DateTimeField(
        default=datetime.now()
    )
    deadline = models.DateField(
        blank=True,
        null=True
    )
    description = models.TextField(
        max_length=200,
        blank=True
    )
    status = models.CharField(
        choices=GOAL_STATUS_CHOICES,
        default=DEFAULT_GOAL_STATUS_CHOICE,
        max_length=15
    )

    @property
    def status_badge_class(self):
        mapping = {
            "in_progress": "bg-warning",
            "completed": "bg-success"
        }
        return mapping.get(self.status.lower(), "bg-secondary")
    
    def __str__(self):
        return f"Goal: {self.name}"
    
    class Meta:
        verbose_name_plural = "Goals"


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"Category: {self.name}"
    
    class Meta:
        verbose_name_plural = "Expense Categories"


class ExpenseSubcategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subcategories"
    )

    def __str__(self):
        if self.category:
            return f"Subcategory: {self.name} > {self.category.name}"
        else:
            return f"Subcategory: {self.name} > NOT SET"
    
    class Meta:
        verbose_name_plural = "Expense Subcategories"


class IncomeSource(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"Source: {self.name}"
    
    class Meta:
        verbose_name_plural = "Income Sources"


class ExpenseRecord(models.Model):
    date = models.DateField()
    value = models.DecimalField(
        decimal_places=2,
        max_digits=7
    )
    currency = models.CharField(
        max_length=3,
        default="eur",
        blank=True
    )
    title = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=100,
        blank=True
    )
    category = models.ForeignKey(
        ExpenseCategory,
        related_name="category_records",
        on_delete=models.SET_NULL,
        null=True
    )
    subcategory = models.ForeignKey(
        ExpenseSubcategory,
        related_name="subcategory_records",
        on_delete=models.SET_NULL,
        null=True
    )
    goal = models.ForeignKey(
        Goal,
        related_name="expenses",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"Expense: ({self.id}){self.title}"
    
    class Meta:
        verbose_name_plural = "Expense Records"


class IncomeRecord(models.Model):
    date = models.DateField()
    source = models.ForeignKey(
        IncomeSource,
        related_name="income_records",
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField(
        max_length=100,
        blank=True
    )
    value = models.DecimalField(
        decimal_places=2,
        max_digits=7
    )
    currency = models.CharField(
        max_length=3,
        default="eur",
        blank=True
    )

    def __str__(self):
        return f"Income: ({self.id}){self.source.name}"
    
    class Meta:
        verbose_name_plural = "Income Records"
