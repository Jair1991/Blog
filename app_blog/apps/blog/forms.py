# all config # #<!--11-->
from django import forms
from .models import Post


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'content', 'image')
