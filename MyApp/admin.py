from django.contrib import admin
from MyApp.models import Product, Catergory, CartOder, CartOderItems, ProductImages, Vendor, order_img

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'product_image', 'description', 'price', 'product_status', 'pid']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status']

class CartOrderItemsAdmin(admin.ModelAdmin):
   list_display = ['order', 'invoice_no', 'item', 'qty', 'image','qty', 'price', 'total']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']

admin.site.register(Product,ProductAdmin)
admin.site.register(Catergory,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(CartOder,CartOrderAdmin)
admin.site.register(CartOderItems,CartOrderItemsAdmin)

