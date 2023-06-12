from django.contrib import admin
from .models import Category, SubCategory, Files

# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminSubCategory(admin.ModelAdmin):
    list_display = ('name', 'category', 'date_added')

class AdminFile(admin.ModelAdmin):
    list_display = ('title', 'image', 'date_added', 'sub_category' )

admin.site.register(Files, AdminFile)
admin.site.register(SubCategory, AdminSubCategory)
admin.site.register(Category, AdminCategory)