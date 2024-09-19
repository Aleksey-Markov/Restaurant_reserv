from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1')
        labels = {
                'email': 'Почта',
                'password1': 'Пароль',
            }
        help_texts = {
                'email': 'Введите вашу почту',
                'password1': 'Введите ваш пароль',
            }


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'phone')
        labels = {
                'email': 'Почта',
                'name': 'Имя',
                'phone': 'Телефон',
            }
