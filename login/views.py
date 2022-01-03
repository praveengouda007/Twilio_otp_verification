from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.exceptions import status
from .verify import *
from rest_framework import status
import pdb
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin,\
    DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import permissions
from django.http import JsonResponse

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
            return Response('Your Num is verified', status=status.HTTP_200_OK)
        else:
            return Response('Incorrect OTP, Please try again', status=status.HTTP_400_BAD_REQUEST)


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
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class Userlist(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserUpdate(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk , format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            phone = request.data['phone']
            ph = send(phone)
            print(ph)
        return Response(serializer.data)

    # def delete(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class UserVerify(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            phone = request.data['phone']
            code = request.data['code']
            verify = check(phone, code)

            print(verify)
            if verify:
                return Response('Your Num is verified', status=status.HTTP_200_OK)
            else:
                return Response('Incorrect OTP, Please try again', status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)
