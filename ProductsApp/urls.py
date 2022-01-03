from .views import ProductView, BrandView, Uploading_csv
from django.conf.urls import url
from django.urls import path
from ProductsApp import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('brand/', BrandView.as_view()),
    path('list/', ProductView.as_view()),
    path('upload/', Uploading_csv.as_view()),
    path('export/', views.export_products_csv),
]