from django.urls import path
from .views import RegisterNewUserView, UserPanelView

urlpatterns = [
    path('signup/', RegisterNewUserView.as_view(), name='signup'),
    path('users/', UserPanelView.as_view(), name = 'allUsers')
]