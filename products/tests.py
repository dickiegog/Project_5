from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product, Category
from cart.models import Cart, CartItem
from checkout.models import Order, OrderItem
from home.models import Comment
from decimal import Decimal

class ProductModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Supplements")
        self.product = Product.objects.create(
            category=self.category,
            name="Protein Powder",
            description="Whey protein for muscle growth",
            price=29.99
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), "Protein Powder")

    def test_product_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url(), f"/products/{self.product.pk}/")
