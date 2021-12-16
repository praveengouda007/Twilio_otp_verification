from django.db import models
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)
    name = models.FileField(null=True, blank=True, upload_to='image/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand
