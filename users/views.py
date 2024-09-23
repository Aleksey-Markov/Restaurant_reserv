from django.views.generic import CreateView, UpdateView
from users.models import User
from tables.models import Table
from django.urls import reverse_lazy
from users.forms import UserRegisterForm, UserProfileForm, TableForm
from django.forms import inlineformset_factory


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        TableFormset = inlineformset_factory(
            User, Table, form=TableForm, extra=1
        )
        if self.request.method == 'POST':
            context_data['formset'] = TableFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data['formset'] = TableFormset(instance=self.object)
        return context_data
