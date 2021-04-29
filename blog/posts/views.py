from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from posts.models import Post

# Create your views here.

# class PostsCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'posts/new.html'
#     form_class = PostForm
#     success_url = reverse_lazy('/')


class PostsFeedView(ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 20
    context_object_name = 'posts'