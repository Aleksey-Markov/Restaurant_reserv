from django.views.generic import CreateView, UpdateView
from users.models import User
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserProfileForm


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    fields = ['email', 'password', 'phone', 'name']
    success_url = reverse_lazy('')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
