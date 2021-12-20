from .views import ProductView, BrandView, FileUploadView
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register("Product_name/", ProductUpload, basename='Product')
# router.register("brand", BrandView)
# router.register("prod", ProductView)
# urlpatterns = router.urls

urlpatterns = [
    path('brand/', BrandView.as_view()),
    path('list/', ProductView.as_view()),
    path('upload/', FileUploadView.as_view()),
]