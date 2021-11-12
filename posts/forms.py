from django import forms
from categories.models import Category
from .models import Post, Comment


class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    description = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'description', 'image', 'body', 'category']


class CommentForm(forms.ModelForm):
    content = forms.CharField()

    class Meta:
        model = Comment
        fields = ['content']


class SearchingForm(forms.Form):
    title = forms.CharField(max_length=100)


class SearchingByDescriptionForm(forms.Form):
    description = forms.CharField(max_length=255)
