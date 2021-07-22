from django.forms import fields
from .models import Company
from django import forms



class GetCompanyDataRangeForm(forms.Form):
    company_name = forms.ModelChoiceField(queryset=Company.objects.all())
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

