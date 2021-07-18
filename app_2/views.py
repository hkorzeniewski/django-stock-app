from rest_framework.fields import ModelField
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CompanySerializer, PricesSerializer
from .models import Company, Prices
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response


from django.shortcuts import render, redirect

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from django.views.generic.edit import FormView

from .forms import GetCompanyDataRangeForm
# Create your views here.


def table_view(request):
    return render(request, 'table.html', {})


# def form_view(request):
#     form = GetCompanyDataRangeForm(request.POST or None)
#     print(form)
#     if form.is_valid():
#         print(form)
#     return render(request, "form.html", {"form": form})

class CompanyView(FormView):
    # model = Company
    form_class = GetCompanyDataRangeForm
    template_name = 'form.html'
    success_url = 'table'


    def form_valid(self, form):
        # context['form'] = form
        company_name = form.cleaned_data.get("company_name")
        start_date = form.cleaned_data.get("start_date")
        end_date = form.cleaned_data.get("end_date")
        print(company_name, start_date, end_date)
        return redirect('/table')


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]

class PricesViewSet(ModelViewSet):
    queryset = Prices.objects.all()
    serializer_class = PricesSerializer
