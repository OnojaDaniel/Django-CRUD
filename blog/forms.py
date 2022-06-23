from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Post

class BlogForms(forms):
    class Meta:
        model = Post
        fields = [
            "title",
            "author",
            "body",
            "publish",
            "status"
        ]