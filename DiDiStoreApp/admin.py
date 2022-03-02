from django.contrib import admin
from .models import *


# Register your models here.
class AdminCat(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class AdminAuthor(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class AdminBook(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    list_editable = ['price',]
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Author, AdminAuthor)
admin.site.register(Book, AdminBook)
admin.site.register(Category, AdminCat)
admin.site.register(MainCategory)