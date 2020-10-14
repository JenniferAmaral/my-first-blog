from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        # qual modelo devera ser usado pracriar esse form
        model = Post
        fields = ('title', 'text',)
