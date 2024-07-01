from django.contrib import admin

from catalog.models import Product, Category, Version


# admin.site.register(Product)
# admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category', 'owner')
    search_fields = ('name', "description",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ("version_number",)
