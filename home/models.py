from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Category  # Update this path based on your app names

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links comment to a user
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Links to product category
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)  # Optional product link
    content = models.TextField()  # The comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the comment is created

    def __str__(self):
        return f'Comment by {self.user.username} on {self.created_at}'
