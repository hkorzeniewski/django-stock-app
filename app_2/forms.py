from django.forms import fields
from .models import Company
from django import forms


class GetCompanyDataRangeForm(forms.Form):
    company_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }))
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control"
            }
        )
    )

# class CompanyForm(forms.ModelForm):
#     class Meta:
#         model = Company
#         fields = ['company_name', 'start_date', 'end_date']