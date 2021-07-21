from django.contrib import admin
from .models import Company, Prices
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    using = 'company_db'

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Prices, CompanyAdmin)
