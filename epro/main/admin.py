from django.contrib import admin
from .models import electric_product , catagory , brand ,ProductDetail, product_galary , rating
@admin.register(electric_product)
class Productadmin(admin.ModelAdmin):
 list_display = ['id']
     
admin.site.register(catagory)
admin.site.register(brand)
admin.site.register(ProductDetail)
admin.site.register(product_galary)
admin.site.register(rating)