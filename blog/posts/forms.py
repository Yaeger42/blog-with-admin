# Django imports
from django import forms

# Model imports
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('user', 'title', 'category', 'image', 'body', 'facebookVideoLink', 'facebookLiveVideoLink', 'eventDateTime', 'eventType')
