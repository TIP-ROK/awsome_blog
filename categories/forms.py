from django import forms
from .models import Category


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)


class CategoryAddingForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['name']
