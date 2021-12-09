from django.shortcuts import render
from .serializers import UserSerializer,VerifySerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from django.conf import settings 
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.exceptions import status
from .verify import *
import pdb


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        phone = request.data['phone']
        ph = send(phone)
        print(ph)
        return Response({'details': 'please check otp'})


class Otp(APIView):
    def post(self, request):

        phone = request.data['phone']
        code = request.data['code']
        verify = check(phone, code)

        print(verify)
        if verify:
            return Response(phone+' is verified successfully')
        else:
<<<<<<< HEAD
            return Response('Incorrect OTP, Please try again', status=status.HTTP_400_BAD_REQUEST)
=======
            return Response('Incorrect OTP', status=status.HTTP_400_BAD_REQUEST)
>>>>>>> bb01b8703d5ef1ce9f5adab1924b3fbf93ca1136


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        token = jwt.encode({
            'id': user.id,
            },
            'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):
    
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
    
        try:
            payload = jwt.decode(token, 'secret',algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
