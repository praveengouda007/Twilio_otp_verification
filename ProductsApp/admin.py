from django.contrib import admin
from import_export import resources
from ProductsApp.models import Product, Brand
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin

# # Register your models here.
# class ProductResource(resources.ModelResource):
#     full_title = Field()
#
#     class Meta:
#         model = Product
#
#     def dehydrate_name(self, product):
#         product_name = getattr(product, "name")
#         return "%s " % (product_name)
#
# class ProductAdmin(ImportExportModelAdmin):
#     resource_class = ProductResource
#
#
# admin.site.register(ProductAdmin)
admin.site.register(Product)
admin.site.register(Brand)

