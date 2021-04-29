from django.urls import path 

from posts import views

urlpatterns = [
    path(
        route = '',
        view = views.PostsFeedView.as_view(),
        name = 'feed'
    ),
]