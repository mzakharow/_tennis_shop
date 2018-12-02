from django.contrib import admin
from ecomapp.models import Category, Brand, Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # автоматическое заполнение поле slug в админке


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)

# Register your models here.
