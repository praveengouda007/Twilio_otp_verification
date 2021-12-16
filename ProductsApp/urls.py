from .views import Productapi, Brandapi
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('b/', Brandapi.as_view({'post': 'create'})),
    url('upload/', Productapi.as_view(), name='file-upload'),
]