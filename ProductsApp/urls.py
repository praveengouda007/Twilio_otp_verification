from .views import ProductView, BrandView, Uploading_csv
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from ProductsApp import views
from django.views.decorators.csrf import csrf_exempt

# router = routers.SimpleRouter()
# router.register("Product_name/", ProductUpload, basename='Product')
# router.register("brand", BrandView)
# router.register("prod", ProductView)
# urlpatterns = router.urls

urlpatterns = [
    path('brand/', BrandView.as_view()),
    path('list/', ProductView.as_view()),
    path('upload/', Uploading_csv.as_view()),
    path('export/', views.export_products_csv),

    # path('ex/', views.exportapi),
]