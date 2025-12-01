from django.db import models


DEFAULT_CURRENCY = "eur"


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
        return f"{self.name}"
    
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