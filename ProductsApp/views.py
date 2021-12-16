import io
from django.shortcuts import render
from rest_framework import generics
from .serializer import ProductSerializer, BrandSerializer
import csv
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.exceptions import status
from rest_framework import viewsets
from .models import Brand, Product
import time

# Create your views here.
class Brandapi(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer



class Productapi(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    file_serializer = ProductSerializer(data=request.data)

    if file_serializer.is_valid():
        time.sleep(10) #2 minutes time delay for process

        file_serializer.save()

        return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

