from django.contrib import admin
from .models import Products, Order

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Site Shopping"
admin.site.index_title = "Manage Site Shopping"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
         queryset.update(catgory="default")

    change_category_to_default.short_description = 'Default Cat'
    list_display = ('title', 'price', 'discount_price', 'catgory',)
    search_fields = ('catgory',)
    actions = ('change_category_to_default',)
    fields = ('title', 'price',)
    list_editable = ('price',)

# Register your models here.
admin.site.register(Products, ProductAdmin)
admin.site.register(Order)