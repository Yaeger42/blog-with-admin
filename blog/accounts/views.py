from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_views


@method_decorator(staff_member_required, name='dispatch')
class RegisterNewUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@method_decorator(staff_member_required, name='dispatch')
class UserPanelView(LoginRequiredMixin, ListView):
    template_name = 'accounts/listUsers.html'
    model = User 
    context_object_name = 'users'


@method_decorator(staff_member_required, name='dispatch')
class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    context_object_name = 'user'
    template_name = 'accounts/edit.html'
    success_url = '/accounts/users/'


@method_decorator(staff_member_required, name = 'dispatch')
class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = '/accounts/users/'