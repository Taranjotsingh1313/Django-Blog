from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class contacadmin(admin.ModelAdmin):
    list_display = [
        'id',
        'Name',
        'email',
    ]
