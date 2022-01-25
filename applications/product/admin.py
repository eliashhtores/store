from django.contrib import admin
from .models import Product, Color


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'price', 'stock')
    list_filter = ('name', 'cost', 'price', 'stock')
    search_fields = ('name', 'cost', 'price')
    ordering = ('name', 'cost', 'price', 'stock')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
