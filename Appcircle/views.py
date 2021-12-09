from .models import *
from .serializers import *
from rest_framework import viewsets


class CircleUserView(viewsets.ModelViewSet):
    queryset = CircleUser.objects.all()
    serializer_class = CircleUserSerializer

class CircleView(viewsets.ModelViewSet):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

