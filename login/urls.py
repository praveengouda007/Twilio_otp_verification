from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('register/', RegisterView.as_view()),     # When user registers sends otp
    path('otp-verify/', Otp.as_view()),            # Verify otp
    path('login/', LoginView.as_view()),           # login with email and password,generates jwt token & saves in cookie
    path('user/', UserView.as_view()),             # token stored in cookie, returns the user details
    path('logout/', LogoutView.as_view()),         # logout
    path('list/', Userlist.as_view()),             # list of users
    path('upd/<int:pk>/', UserUpdate.as_view()),   # updating existing phone number
    path('ver/<int:pk>/', UserVerify.as_view()),   #verifying updated phone number
]
