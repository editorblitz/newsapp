from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'teaser_text', 'content', 'author', 'status', 'auto_generate_slug', 'slug']


#this needs to be imported into models