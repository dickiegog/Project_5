from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order, OrderItem
from products.models import Product, Category

class OrderModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="orderuser", password="testpass")
        self.category = Category.objects.create(name="Equipment")
        self.product = Product.objects.create(
            category=self.category,
            name="Dumbbell",
            description="Strength training",
            price=20.00
        )
        self.order = Order.objects.create(
            user=self.user,
            full_name="Order User",
            email="order@example.com",
            address="1 Main St",
            city="Test City",
            postal_code="00000",
            country="IE",
            phone_number="1234567890",
            total=20.00
        )
        self.item = OrderItem.objects.create(order=self.order, product=self.product, quantity=1, price=20.00)

    def test_order_str(self):
        self.assertEqual(str(self.order), f"Order {self.order.id} - {self.user.username}")
