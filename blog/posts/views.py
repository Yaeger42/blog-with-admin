from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.shortcuts import render

from posts.models import Post
from posts.forms import PostForm

# Create your views here.

class PostsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class PostsFeedView(ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 20
    context_object_name = 'posts'
    
class VideoFeedView(ListView):
    template_name = 'posts/videofeed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 20
    context_object_name = 'posts'

class EventsFeedView(ListView):
    template_name = 'posts/eventsfeed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 20
    context_object_name = 'posts'

class EventsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/events.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:eventsfeed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


def show_info(request):
    return render(request, "posts/info.html", {})
    
def show_contact(request):
    return render(request, "posts/contact.html", {})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:feed')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user = owner)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'category', 'image', 'body']
    context_object_name = 'post'
    template_name = 'posts/edit.html'
    success_url = reverse_lazy('posts:feed')


class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'