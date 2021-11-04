from django.urls import path 

from posts import views
from .views import show_info
urlpatterns = [
    path(
        route = '',
        view = views.PostsFeedView.as_view(),
        name = 'feed'
    ),
    path(
        'posts/info', show_info
    ),
    path(
        route = 'posts/eventsfeed/',
        view = views.EventsFeedView.as_view(),
        name = 'eventsfeed'
    ),
    path(
        route = 'posts/events/',
        view = views.EventsCreateView.as_view(),
        name = 'createevent'
    ),
    path(
        route = 'posts/new/',
        view = views.PostsCreateView.as_view(),
        name = 'create'
    ),

    path(
        route = 'posts/edit/<pk>',
        view = views.PostEditView.as_view(),
        name = 'edit'
    ),

    path(
        route = 'posts/<pk>/delete',
        view = views.PostDeleteView.as_view(),
        name = 'delete'
    ),
    
    path(
        route = 'posts/<pk>',
        view = views.PostDetailView.as_view(),
        name = 'detail'
    )
]