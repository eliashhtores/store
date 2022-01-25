from django.contrib import admin
from .models import Sale, Detail


class SaleAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'state')
    list_filter = ('date', 'amount', 'state')
    search_fields = ('date', 'amount', 'state')
    ordering = ('id',)


class DetailAdmin(admin.ModelAdmin):
    list_display = ('sale', 'product', 'quantity')
    list_filter = ('sale', 'product')
    search_fields = ('sale', 'product')
    ordering = ('id',)


admin.site.register(Sale, SaleAdmin)
admin.site.register(Detail, DetailAdmin)
