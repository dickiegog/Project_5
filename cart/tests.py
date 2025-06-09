from django.test import TestCase
from django.contrib.auth.models import User
from .models import Cart, CartItem
from products.models import Product, Category

class CartModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="cartuser", password="testpass")
        self.category = Category.objects.create(name="Accessories")
        self.product = Product.objects.create(
            category=self.category,
            name="Skipping Rope",
            description="For cardio",
            price=5.00
        )
        self.cart = Cart.objects.create(user=self.user)
        self.item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=3)

    def test_cart_total_price(self):
        self.assertEqual(self.cart.get_total_price(), 15.00)
