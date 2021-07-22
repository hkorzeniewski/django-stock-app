from rest_framework.fields import ModelField
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CompanySerializer, PricesSerializer
from .models import Company, Prices
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from django.views.generic.edit import FormView
from django.http import HttpResponseNotFound
from .forms import GetCompanyDataRangeForm

from sentry_sdk import capture_message


# Create your views here.


def table(request):

    return render(request, 'table.html', {})


class CompanyView(FormView):
    # model = Company
    form_class = GetCompanyDataRangeForm
    template_name = 'form.html'
    success_url = 'table'

    def form_valid(self, form):

        company_name = form.cleaned_data.get("company_name")
        start_date = form.cleaned_data.get("start_date")
        end_date = form.cleaned_data.get("end_date")
        company = Company.objects.get(company_name=company_name)
        print(company.prices.filter(date__range=[start_date, end_date]))
        prices = company.prices.filter(date__range=[start_date, end_date])
        context = {
            "prices": prices,
            "company_name": company_name
        }
        return render(self.request, 'table.html', context=context)
        # return redirect('/table')


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company_name']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]



class PricesViewSet(ModelViewSet):
    queryset = Prices.objects.all()
    serializer_class = PricesSerializer


def permission_denied_view(request):
    raise PermissionDenied


def page_not_found_view(*args, **kwargs):
    capture_message("Page not found", level="error")
    return HttpResponseNotFound("Not found")
