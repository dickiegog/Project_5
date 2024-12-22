from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """Return a friendly representation of the category name."""
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', default='my_PP5/media/products/no image.jpeg')
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.name
