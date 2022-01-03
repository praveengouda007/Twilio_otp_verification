from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('otp/', Otp.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('list/', Userlist.as_view()),
    path('upd/<int:pk>/', UserUpdate.as_view()),
    path('ver/<int:pk>/', UserVerify.as_view()),
    # path('upd/<int:pk>/', Update_num.as_view()),
    # path('upd1/<int:pk>/', Update_num1.as_view()),
    # path('vup/', verify_updnum.as_view()),
]
