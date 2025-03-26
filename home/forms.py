from django import forms
from .models import Comment, NewsletterSignup

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['category', 'product', 'content']

class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ['email']