from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset, Field, Div
from .models import *


class ExpenseRecordForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ExpenseRecordForm, self).__init__(*args, **kwargs)
        
        self.fields["date"].widget = forms.DateInput(attrs={"type": "date"})

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
    def __init__(self, *args, **kwargs):
        super(ExpenseCategoryForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                # WRAPPER (mobile = column, desktop = row)
                Div(
                    # INPUT + LABEL vedľa seba
                    Div(
                        Field("name", placeholder="Enter new category", wrapper_class=" gap-3 mb-0 d-flex flex-row align-items-center flex-md-nowrap flex-wrap mb-0 justify-content-center"),
                        css_class="col-12 col-md-auto d-flex flex-row align-items-center justify-content-center me-3"
                    ),

                    # BUTTON hneď za inputom
                    Div(
                        Submit("submit_category", "ADD", css_class="btn btn-lg form-button"),
                        css_class="col-12 d-flex justify-content-center col-md-auto mt-2 mt-md-0"
                    ),

                    css_class="d-flex flex-column flex-md-row align-items-start"
                ),
            )
        )

        # self.helper.layout = Layout(
        #     Div(
        #         Field("name", wrapper_class="d-flex flex-row align-items-center", placeholder="Enter new category:"),
        #         Submit("submit_category", "ADD", css_class="btn btn-lg form-button"),
        #         css_class="d-flex flex-row flex-wrap align-items-center"

        #     )
        #         # css_class="d-flex flex-column align-items-center justify-content-start gap-2 mt-3 mb-4"
        # )
            # Row(
            #     Column(
            #         Field('name', wrapper_class='d-flex flex-row align-items-center', placeholder="Enter new category"), 
            #         css_class='col-md-3 form-input form-control-lg mb-0'
            #     ),
            #     Column(
            #         Submit("submit_category", "Submit", css_class="col-md-2 btn-lg form-button"),
            #     ),
            #     css_class="align-items-center justify-content-center mt-3 mb-4",
            # ))
        
        self.fields["name"].label = "New expense category:"


    class Meta:
        model = ExpenseCategory
        fields = [
            "name"
        ]


# class ExpenseSubCategoryForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ExpenseSubCategoryForm, self).__init__(*args, **kwargs)
        
#         self.helper = FormHelper(self)
#         # self.helper.layout = Layout(
#         #     Row(
#         #         Column(
#         #             Field('name', wrapper_class='d-flex flex-row align-items-center'), 
#         #             css_class='col-md-3 form-input form-control-lg mb-0'
#         #         ),
#         #         Column(
#         #             Submit("submit_subcategory", "Submit", css_class="col-md-2 btn-lg form-button"),
#         #         ),
#         #         css_class="align-items-center justify-content-center mt-3 mb-4",
#         #     ))
#         self.helper.layout = Layout(
#             Div(
#                 # WRAPPER (mobile = column, desktop = row)
#                 Div(
#                     # INPUT + LABEL vedľa seba
#                     Div(
#                         Field("name", placeholder="Enter new subcategory", wrapper_class=" gap-3 mb-0 d-flex flex-row align-items-center flex-md-nowrap flex-wrap mb-0 justify-content-center"),
#                         css_class="col-12 col-md-auto d-flex flex-row align-items-center justify-content-center me-3"
#                     ),

#                     # BUTTON hneď za inputom
#                     Div(
#                         Submit("submit_subcategory", "ADD", css_class="btn btn-lg form-button"),
#                         css_class="col-12 d-flex justify-content-center col-md-auto mt-2 mt-md-0"
#                     ),

#                     css_class="d-flex flex-column flex-md-row align-items-start"
#                 ),
#             )
#         )

#         self.fields["name"].label = "New expense subcategory:"



    # class Meta:
    #     model = ExpenseSubcategory
    #     fields = [
    #         "name"
    #     ]


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
    def __init__(self, *args, **kwargs):
        super(IncomeSourceForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column(
                    Field('name', wrapper_class='d-flex flex-row align-items-center'), 
                    css_class='col-md-3 form-input form-control-lg mb-0'
                ),
                Column(
                    Reset("reset", "Reset", css_class="col-md-2 btn-danger btn-lg form-button me-4"),
                ),
                Column(
                    Submit("submit", "Submit", css_class="col-md-2 btn-lg form-button"),
                ),
                css_class="align-items-center justify-content-center mt-3 mb-4",
            ))


    class Meta:
        model = IncomeSource
        fields = [
            "name"
        ]