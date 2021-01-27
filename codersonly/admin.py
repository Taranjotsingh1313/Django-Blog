from django.contrib import admin
from .models import blogPost,BlogComment
# Register your models here.


@admin.register(blogPost)
class postadmin(admin.ModelAdmin):
    list_display = ['title', 'author']

@admin.register(BlogComment)
class blogcommentadmin(admin.ModelAdmin):
    list_display = [
        'user'
    ]