from django.urls import path
from .views import RegisterNewUserView, UserPanelView, UserEditView, DeleteUserView
urlpatterns = [
    path(
        route = 'signup/', 
        view = RegisterNewUserView.as_view(), 
        name = 'signup'),

    path(
        route = 'users/', 
        view = UserPanelView.as_view(), 
        name = 'allUsers'),

    path(
        route = 'edit/<pk>', 
        view = UserEditView.as_view(), 
        name = 'edit'),

    path(
        route = '<pk>/delete/',
        view = DeleteUserView.as_view(),
        name = 'delete'
    )
]