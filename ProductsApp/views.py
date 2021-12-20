import io
from django.shortcuts import render
from rest_framework import generics
from .serializer import ProductSerializer, BrandSerializer
from django.core.files.base import ContentFile
import csv
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.exceptions import status
from rest_framework import viewsets
from .models import Brand, Product
from django.core.files.storage import FileSystemStorage
import time
from rest_framework.renderers import JSONRenderer

# Create your views here.
class BrandView(APIView):
    def get(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)



fs = FileSystemStorage(location='file/')

class FileUploadView(APIView):
    def post(self, request):
        file = request.FILES["name"]
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "file.csv", file_content
        )
        c_file = fs.path(file_name)
        csv_file = open(c_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)       # skips one row in csv file i.e., headers

        product_list = []
        for id_, row in enumerate(reader):
            (
                brand,
                name,
                category,
                description,
            ) = row

            product_list.append(
                Product(
                    brand_id=brand,
                    name=name,
                    category=category,
                    description=description,
                )
            )
        Product.objects.bulk_create(product_list)
        time.sleep(10)   #gave only 10 seconds delay for time saving
        return Response("Uploaded Successfully")





