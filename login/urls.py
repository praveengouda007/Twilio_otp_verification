from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('otp/', Otp.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
]
