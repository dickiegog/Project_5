from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get all categories and their friendly names
        categories = Category.objects.all()
        friendly_names = [(cat.id, cat.get_friendly_name()) for cat in categories]

        # Update category field choices
        self.fields['category'].choices = friendly_names

        # Apply Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
