from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset, Field, Div
from .models import *


class ExpenseRecordForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ExpenseRecordForm, self).__init__(*args, **kwargs)
        
        self.fields["date"].widget = forms.DateInput(attrs={"type": "date"})

        self.fields["category"].label_from_instance = lambda obj: obj.name
        self.fields["subcategory"].label_from_instance = lambda obj: obj.name


        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('date', css_class='col-md-3 form-input form-control-lg'),
                Column('title', css_class='col-md-3 form-input form-control-lg'),
                Column('value', css_class='col-md-3 form-input form-control-lg'),
                css_class="justify-content-center",
            ),
            Row(
                Column('category', css_class='col-md-3 form-input form-control-lg'),
                Column('subcategory', css_class='col-md-3 form-input form-control-lg'),
                css_class="justify-content-center",
            ),
            Row(
                Column('description', css_class='col-md-12 form-input form-control-lg has-textarea'),
                css_class="justify-content-center",
            ),
            Row(
                Reset("reset", "Reset", css_class="col-md-2 btn-danger btn-lg form-button me-4"),
                Submit("submit", "Submit", css_class="col-md-2 btn-lg form-button"),
                css_class="justify-content-center mt-3",
            ))


    class Meta:
        model = ExpenseRecord
        fields = [
            "date",
            "title",
            "value",
            "category",
            "subcategory",
            "description"
        ]


class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Field("name",
                          placeholder="Enter new category",
                          wrapper_class="gap-3 d-flex flex-row align-items-center flex-md-nowrap justify-content-center mb-0"),
                    css_class="col-12 col-md-auto d-flex flex-row align-items-center justify-content-center me-3 mb-0"
                ),
                Div(
                    Submit("submit_category_add", "ADD", css_class="btn btn-lg form-button"),
                    css_class="col-12 d-flex justify-content-center col-md-auto mt-2 mt-md-0 align-items-center"
                ),
                css_class="d-flex flex-column flex-md-row align-items-center mb-0"
            )
        )
        self.fields["name"].label = "New expense category:"


class ExpenseSubcategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseSubcategory
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Field("name",
                          placeholder="Enter new subcategory",
                          wrapper_class="gap-3 d-flex flex-row align-items-center flex-md-nowrap justify-content-center mb-0"),
                    css_class="col-12 col-md-auto d-flex flex-row align-items-center justify-content-center me-3 mb-0"
                ),
                Div(
                    Submit("submit_subcategory_add", "ADD", css_class="btn btn-lg form-button"),
                    css_class="col-12 d-flex justify-content-center col-md-auto mt-2 mt-md-0 align-items-center"
                ),
                css_class="d-flex flex-column flex-md-row align-items-center mb-0"
            )
        )
        self.fields["name"].label = "New expense subcategory:"


class IncomeRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IncomeRecordForm, self).__init__(*args, **kwargs)
        
        self.fields["date"].widget = forms.DateInput(attrs={"type": "date"})

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('date', css_class='col-md-3 form-input form-control-lg'),
                Column('source', css_class='col-md-3 form-input form-control-lg'),
                Column('value', css_class='col-md-3 form-input form-control-lg'),
                css_class="justify-content-center",
            ),
            Row(
                Column('description', css_class='col-md-12 form-input form-control-lg has-textarea'),
                css_class="justify-content-center",
            ),
            Row(
                Reset("reset", "Reset", css_class="col-md-2 btn-danger btn-lg form-button me-4"),
                Submit("submit", "Submit", css_class="col-md-2 btn-lg form-button"),
                css_class="justify-content-center mt-3",
            ))


    class Meta:
        model = IncomeRecord
        fields = [
            "date",
            "source",
            "value",
            "description"
        ]


class IncomeSourceForm(forms.ModelForm):
    class Meta:
        model = IncomeSource
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Field("name",
                          placeholder="Enter new source",
                          wrapper_class="gap-3 d-flex flex-row align-items-center flex-md-nowrap justify-content-center mb-0"),
                    css_class="col-12 col-md-auto d-flex flex-row align-items-center justify-content-center me-3 mb-0"
                ),
                Div(
                    Submit("submit_source_add", "ADD", css_class="btn btn-lg form-button"),
                    css_class="col-12 d-flex justify-content-center col-md-auto mt-2 mt-md-0 align-items-center"
                ),
                css_class="d-flex flex-column flex-md-row align-items-center mb-0"
            )
        )
        self.fields["name"].label = "New income source:"
