from django.contrib import admin
from .models import Comment  # Import the Comment model

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'product', 'created_at', 'content')  # Columns to display
    list_filter = ('category', 'created_at')  # Filters for admin
    search_fields = ('content', 'user__username', 'product__name')  # Search functionality
