from django.contrib import admin
from .models import blogPost
# Register your models here.


@admin.register(blogPost)
class postadmin(admin.ModelAdmin):
    list_display = ['title', 'author']
