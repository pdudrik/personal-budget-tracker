from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, TemplateView, FormView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .utils import valid_int_id
from .models import *
from .forms import *


#------------------------ EXPENSE ------------------------#
class ExpenseListView(ListView):
    template_name = "budget/expense_list.html"
    model = ExpenseRecord
    context_object_name = "records"


class ExpenseAddView(FormView):
    template_name = "budget/expense_add.html"
    # model = ExpenseRecord
    form_class = ExpenseRecordForm
    success_url = reverse_lazy("budget:expense-list")


    def form_valid(self, form):
        form.save()
        print(f"SUCCESS: expense record {form.instance.title} saved!")
        return super().form_valid(form)
    

    def form_invalid(self, form):
        print(f"ERROR: failed to save expense record {form.instance.title}!")
        print(form.errors.as_json())
        return super().form_invalid(form)


class ExpenseUpdateView(UpdateView):
    template_name = "budget/expense_update.html"
    model = ExpenseRecord
    form_class = ExpenseRecordForm
    success_url = reverse_lazy("budget:expense-list")


class ExpenseDeleteView(DeleteView):
    model = ExpenseRecord
    success_url = reverse_lazy("budget:expense-list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    


#------------------------ EXPENSE CATEGORY ------------------------#
class ExpenseCategoryDeleteView(View):
    def post(self, request):
        print(request.POST)
        # category_id = request.POST.get("category_delete_select")
        # category = get_object_or_404(ExpenseCategory, pk=category_id)
        # print(category.name)
        # pk = request.POST.get("category_delete_select")
        # print(f"PK: {pk}")

        # if pk:
        #     item = ExpenseCategory.objects.get(pk=pk)
        #     category_name = item.name

        #     item.delete()
        #     print(f"SUCCESS: category record {category_name} deleted!")

        return redirect("budget:settings")


#------------------------ EXPENSE SUBCATEGORY ------------------------#
class ExpenseSubcategoryDeleteView(DeleteView):
    def post(self, request, pk):
        ExpenseSubcategory.objects.filter(pk=pk).delete()
        return redirect("budget:settings")


#------------------------ INCOME SOURCE ------------------------#
class IncomeSourceListView(ListView):
    template_name = "budget/income_source_list.html"
    model = IncomeSource
    context_object_name = "records"

    def get_context_data(self, **kwargs):
        context = super(IncomeSourceListView, self).get_context_data(**kwargs)
        context['form'] = IncomeSourceForm
        return context


# class IncomeSourceAddView(FormView):
#     template_name = "budget/income_add.html"
#     form_class = IncomeSourceForm
#     success_url = reverse_lazy("budget:income-list")


#     def form_valid(self, form):
#         form.save()
#         print(f"SUCCESS: income record {form.instance.source} saved!")
#         return super().form_valid(form)
    

#     def form_invalid(self, form):
#         print(f"ERROR: failed to save income record {form.instance.source}!")
#         print(form.errors.as_json())
#         return super().form_invalid(form)


# class IncomeSourceUpdateView(UpdateView):
#     template_name = "budget/income_update.html"
#     model = IncomeSource
#     form_class = IncomeSourceForm
#     success_url = reverse_lazy("budget:income-list")


# class IncomeSourceDeleteView(DeleteView):
#     model = IncomeSource
#     success_url = reverse_lazy("budget:income-list")

#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)
    

#------------------------ INCOME ------------------------#
class IncomeListView(ListView):
    template_name = "budget/income_list.html"
    model = IncomeRecord
    context_object_name = "records"


class IncomeAddView(FormView):
    template_name = "budget/income_add.html"
    form_class = IncomeRecordForm
    success_url = reverse_lazy("budget:income-list")


    def form_valid(self, form):
        form.save()
        print(f"SUCCESS: income record {form.instance.source} saved!")
        return super().form_valid(form)
    

    def form_invalid(self, form):
        print(f"ERROR: failed to save income record {form.instance.source}!")
        print(form.errors.as_json())
        return super().form_invalid(form)


class IncomeUpdateView(UpdateView):
    template_name = "budget/income_update.html"
    model = IncomeRecord
    form_class = IncomeRecordForm
    success_url = reverse_lazy("budget:income-list")


class IncomeDeleteView(DeleteView):
    model = IncomeRecord
    success_url = reverse_lazy("budget:income-list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
        

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {"form": self.form})
    
    # def post(self, request, *args, **kwargs):
    #     obj = self.form(request.POST)

    #     if obj.is_valid():
    #         obj.save()

    #         print(f"SUCCESS: expense record {obj.instance.title} saved!")
    #         # print("SUCCESS")
        
    #     else:
    #         print(f"ERROR: failed to save expense record {obj.instance.title}!")
    #         # print("ERROR")
        
    #     return redirect("budget:expense-list")


#------------------------ SETTINGS ------------------------#
class SettingsView(TemplateView):
    template_name = "budget/settings.html"
    category_form = ExpenseCategoryForm(prefix="category")
    subcategory_form = ExpenseSubcategoryForm(prefix="subcategory")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "category_form": self.category_form,
            "subcategory_form": self.subcategory_form,
            "category_list": ExpenseCategory.objects.all(),
            "subcategory_list": ExpenseSubcategory.objects.all()
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

        
        return redirect("budget:settings")