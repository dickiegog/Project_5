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


class CartTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(name="Accessories")
        self.product = Product.objects.create(
            category=self.category,
            name="Resistance Band",
            description="Ideal for workouts",
            price=9.99
        )
        self.cart = Cart.objects.create(user=self.user)
        self.item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_cart_total_price(self):
        self.assertEqual(self.cart.get_total_price(), Decimal("19.98"))

    def test_cart_item_total_price(self):
        self.assertAlmostEqual(Decimal(self.item.get_total_price()), Decimal("19.98"))


class CheckoutOrderTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="buyer", password="testpass")
        self.category = Category.objects.create(name="Equipment")
        self.product = Product.objects.create(
            category=self.category,
            name="Yoga Mat",
            description="Eco-friendly mat",
            price=19.99
        )
        self.order = Order.objects.create(
            user=self.user,
            full_name="Test Buyer",
            email="buyer@example.com",
            phone="1234567890",
            address="123 Street",
            city="Testville",
            postal_code="12345",
            country="IE",
            phone_number="1234567890",
            total=19.99
        )
        self.item = OrderItem.objects.create(order=self.order, product=self.product, quantity=1, price=19.99)

    def test_order_str(self):
        self.assertEqual(str(self.order), f"Order {self.order.id} - {self.user.username}")

    def test_order_item_str(self):
        self.assertEqual(str(self.item), "Yoga Mat x 1")


class HomeCommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="commenter", password="testpass")
        self.category = Category.objects.create(name="Nutrition")
        self.product = Product.objects.create(
            category=self.category,
            name="Multivitamins",
            description="Daily health boost",
            price=12.99
        )
        self.comment = Comment.objects.create(
            user=self.user,
            category=self.category,
            product=self.product,
            content="Really effective!"
        )

    def test_comment_str(self):
        self.assertIn("commenter", str(self.comment))


class ProductViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Gear")
        self.product = Product.objects.create(
            category=self.category,
            name="Water Bottle",
            description="Stay hydrated",
            price=5.99
        )

    def test_product_catalog_view(self):
        response = self.client.get(reverse("products:product_catalog"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/catalog.html")

    def test_product_detail_view(self):
        response = self.client.get(reverse("products:product_detail", args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
