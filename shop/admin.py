from django.contrib import admin
from shop.models import Category, Brand, Product, CartItem, Cart, Order


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # автоматическое заполнение поле slug в админке


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']     # зададим поля, которые можно редактировать на странице спимка
    prepopulated_fields = {'slug': ('name', )}   # автоматическое заполнение поле slug в админке


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
