from django.contrib import admin
from .models import customer, category, product, purchase, purchase_item

class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Customer Details',     {'fields': ['name']}),
        (None,                   {'fields': ['phone']}),

    ]
    list_display =  ('date_joined','name','phone')
    #list_filter = ['date_time']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category Details',    {'fields': ['category_name']}),
        (None,                  {'fields': ['other_details']}),
    ]
    list_display =  ('category_name','other_details')
    search_fields = ['category_name']
    #list_filter = ['category_name']

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product Details',    {'fields': ['product_name']}),
        (None,                  {'fields': ['product_image']}),
        (None,                  {'fields': ['price']}),
        (None,                  {'fields': ['product_category']}),
    ]
    list_display =  ('product_name','product_image','price','product_category')
    search_fields = ['product_name']
    list_filter = ['price']

class PurchaseAdmin(admin.ModelAdmin):
    fieldsets = [
        #('Purchase Details',     {'fields': ['date']}),
        ('Purchase Details',                   {'fields': ['customer_id']}),
        ]
    list_display =  ('date','customer_id')

class Purchase_Item_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Purchased Items',    {'fields': ['purchase_date']}),
        (None,                  {'fields': ['purchase_id']}),
        (None,                  {'fields': ['product_id']}),
        (None,                  {'fields': ['price']}),
        (None,                  {'fields': ['quantity']}),
        
    ]
    list_display =  ('purchase_date','purchase_id','product_id','price','quantity','total_price')
    #search_fields = ['product_name']
    #list_filter = ['price']

admin.site.register(customer, CustomerAdmin)
admin.site.register(category, CategoryAdmin)
admin.site.register(product, ProductAdmin)
admin.site.register(purchase, PurchaseAdmin)
admin.site.register(purchase_item, Purchase_Item_Admin)

# Register your models here.
