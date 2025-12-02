import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, TemplateView, FormView, UpdateView, DeleteView, View, CreateView
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from .utils import valid_int_id, get_categories_json
from .models import *
from .forms import *


class HomeView(TemplateView):
    template_name = "budget/index.html"


#------------------------ EXPENSE ------------------------#
class ExpenseListView(ListView):
    template_name = "budget/expense_list.html"
    model = ExpenseRecord
    context_object_name = "records"


class ExpenseAddView(CreateView):
    template_name = "budget/expense_add.html"
    model = ExpenseRecord
    form_class = ExpenseRecordForm
    success_url = reverse_lazy("budget:expense-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_json"] = mark_safe(json.dumps(get_categories_json()))
        context["category_list"] = ExpenseCategory.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, f"Expense record \"{form.instance.title}\" added successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors.as_json())
        messages.error(self.request, "Expense record coundn't be added!")
        return super().form_invalid(form)


class ExpenseUpdateView(UpdateView):
    template_name = "budget/expense_update.html"
    model = ExpenseRecord
    form_class = ExpenseRecordForm
    success_url = reverse_lazy("budget:expense-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_json"] = mark_safe(json.dumps(get_categories_json()))
        return context
    
    def form_valid(self, form):
        messages.success(self.request, f"Expense record {form.instance.title} updated successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors.as_json())
        messages.error(self.request, "Couldn't update expense record!")
        return super().form_invalid(form)


class ExpenseDeleteView(DeleteView):
    model = ExpenseRecord
    success_url = reverse_lazy("budget:expense-list")

    def get(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(request, f"Expense record \"{self.get_object().title}\" deleted successfully!")
        return super().post(request, *args, **kwargs)
    

#------------------------ INCOME ------------------------#
class IncomeListView(ListView):
    template_name = "budget/income_list.html"
    model = IncomeRecord
    context_object_name = "records"


class IncomeAddView(CreateView):
    template_name = "budget/income_add.html"
    form_class = IncomeRecordForm
    success_url = reverse_lazy("budget:income-list")

    def form_valid(self, form):
        messages.success(self.request, f"Income record from \"{form.instance.source}\" added successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors.as_json())
        messages.error(self.request, "Income record coundn't be added!")
        return super().form_invalid(form)


class IncomeUpdateView(UpdateView):
    template_name = "budget/income_update.html"
    model = IncomeRecord
    form_class = IncomeRecordForm
    success_url = reverse_lazy("budget:income-list")

    def form_valid(self, form):
        messages.success(self.request, f"Income record from \"{form.instance.source.name}\" updated successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors.as_json())
        messages.error(self.request, "Couldn't update income record!")
        return super().form_invalid(form)


class IncomeDeleteView(DeleteView):
    model = IncomeRecord
    success_url = reverse_lazy("budget:income-list")

    def get(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(request, f"Income record from \"{self.get_object().source.name}\" deleted successfully!")
        return super().post(request, *args, **kwargs)


#------------------------ SETTINGS ------------------------#
class SettingsView(TemplateView):
    template_name = "budget/settings.html"
    category_form = ExpenseCategoryForm(prefix="category")
    subcategory_form = ExpenseSubcategoryForm(prefix="subcategory")
    source_form = IncomeSourceForm(prefix="source")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "category_form": self.category_form,
            "subcategory_form": self.subcategory_form,
            "source_form": self.source_form,
            "category_list": ExpenseCategory.objects.all(),
            "subcategory_list": ExpenseSubcategory.objects.all(),
            "source_list": IncomeSource.objects.all(),
        })
    
    def post(self, request, *args, **kwargs):
        ### CATEGORY ###
        if "submit_category_add" in request.POST:
            form = ExpenseCategoryForm(request.POST, prefix="category")
            if form.is_valid():
                form.save()
                messages.success(request, "New category added successfully!")

        elif "submit_category_update" in request.POST:
            category_id = valid_int_id(request.POST.get("category_id"))
            new_category_name = request.POST.get("category-name")
            
            if not category_id:
                messages.error(request, "Invalid category ID format!")
                return redirect("budget:settings")

            try:
                category_record = ExpenseCategory.objects.get(id=category_id)
                category_record.name = new_category_name
                category_record.save()
                messages.success(request, "Category name changed successfully!")
            
            except ExpenseCategory.DoesNotExist:
                messages.error(request, "Selected subcategory does not exist!")
        
        elif "submit_category_delete" in request.POST:
            category_id = valid_int_id(request.POST.get("category_id"))

            if not category_id:
                messages.error(request, "Invalid category ID format!")
                return redirect("budget:settings")

            try:
                category_record = ExpenseCategory.objects.get(id=category_id)
                category_record.delete()
                messages.success(request, "Category deleted successfully!")

            except ExpenseCategory.DoesNotExist:
                messages.error(request, "Couldn't delete selected category. Category not found.")


        ### SUBCATEGORY ###
        elif "submit_subcategory_add" in request.POST:
            form = ExpenseSubcategoryForm(request.POST, prefix="subcategory")
            if form.is_valid():
                form.save()
                messages.success(request, "New subcategory added successfully!")

        elif "submit_subcategory_update" in request.POST:
            subcategory_id = valid_int_id(request.POST.get("subcategory_id"))
            new_name = request.POST.get("subcategory-name")
            category_id = valid_int_id(request.POST.get("subcategory_category_id"))

            if not subcategory_id or not category_id:
                messages.error(request, "Invalid category or subcategory ID format!")
                return redirect("budget:settings")

            save_record = False
            try:
                subcategory_record = ExpenseSubcategory.objects.get(id=subcategory_id)
                if subcategory_record.name != new_name:
                    subcategory_record.name = new_name
                    save_record = True
                    messages.success(request, "Subcategory name changed successfully!")

                if not subcategory_record.category or subcategory_record.category.id != category_id:
                    try:
                        target_category = ExpenseCategory.objects.get(pk=category_id)
                        subcategory_record.category = target_category
                        save_record = True
                        messages.success(request, "Selected parent category for subcategory updated successfully!")
            
                    except ExpenseCategory.DoesNotExist:
                        messages.error(request, "Selected category you wanted to assign as parent category for subcategory does not exist!") 

                if save_record:
                    subcategory_record.save()   
                else:
                    messages.info(request, "No changes applied to subcategories.")                   
            
            except ExpenseSubcategory.DoesNotExist:
                messages.error(request, "Selected subcategory does not exist!")

        
        elif "submit_subcategory_delete" in request.POST:
            subcategory_id = valid_int_id(request.POST.get("subcategory_id"))

            if not category_id:
                messages.error(request, "Invalid subcategory ID format!")
                return redirect("budget:settings")

            try:
                subcategory_record = ExpenseSubcategory.objects.get(id=subcategory_id)
                subcategory_record.delete()
                messages.success(request, "Subcategory deleted successfully!")

            except ExpenseSubcategory.DoesNotExist:
                messages.error(request, "Couldn't delete selected subcategory. Subcategory not found.")
    

        ### INCOME SOURCE ###
        elif "submit_source_add" in request.POST:
            form = IncomeSourceForm(request.POST, prefix="source")
            if form.is_valid():
                form.save()
                messages.success(request, "New source added successfully!")

        elif "submit_source_update" in request.POST:
            source_id = valid_int_id(request.POST.get("source_id"))
            new_source_name = request.POST.get("source-name")
            
            if not source_id:
                messages.error(request, "Invalid source ID format!")
                return redirect("budget:settings")

            try:
                source_record = IncomeSource.objects.get(id=source_id)
                source_record.name = new_source_name
                source_record.save()
                messages.success(request, "Source name changed successfully!")
            
            except IncomeSource.DoesNotExist:
                messages.error(request, "Selected source does not exist!")
        
        elif "submit_source_delete" in request.POST:
            source_id = valid_int_id(request.POST.get("source_id"))

            if not source_id:
                messages.error(request, "Invalid source ID format!")
                return redirect("budget:settings")

            try:
                source_record = IncomeSource.objects.get(id=source_id)
                source_record.delete()
                messages.success(request, "Source deleted successfully!")

            except IncomeSource.DoesNotExist:
                messages.error(request, "Couldn't delete selected source. Source not found.")

    
        return redirect("budget:settings")
    
