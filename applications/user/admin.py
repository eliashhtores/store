from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'city')
    list_filter = ('gender',)
    search_fields = ('email', 'full_name', 'city')
    ordering = ('full_name', 'email')


admin.site.register(User, UserAdmin)
