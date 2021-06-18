from django.contrib import admin

# Register your models here.
from photos.models import Category, Photos


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Photos)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'image', 'date']
