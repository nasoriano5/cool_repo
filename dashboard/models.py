from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=50, null=True)
    link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
class Product(models.Model):
    name = models.CharField(max_length= 50, null=True)
    product_type = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

