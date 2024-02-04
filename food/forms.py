from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # Fix the typo here
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
