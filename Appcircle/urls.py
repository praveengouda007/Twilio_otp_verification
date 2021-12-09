from django.contrib import admin
from django.urls import path, include
from Appcircle import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('CircleUser', views.CircleUserView)
router.register('Circle', views.CircleView)


urlpatterns = [
    path('', include(router.urls))
]