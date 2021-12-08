from .models import Comment
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'rating')