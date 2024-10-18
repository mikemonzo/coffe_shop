from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.TextField(max_length=2083, verbose_name="Product Description")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Product Price"
    )
    available = models.BooleanField(default=True, verbose_name="Product Availability")
    # stock = models.IntegerField(verbose_name="Product Stock")
    image = models.ImageField(upload_to="logs", null=True, blank=True, verbose_name="Product Image")

    def __str__(self):
        return str(self.name)
