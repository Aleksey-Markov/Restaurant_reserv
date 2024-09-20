from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'phone', 'password1', 'password2')
        labels = {
                'email': 'Почта',
                'password1': 'Пароль',
                'password2': 'Подтвердите пароль',
            }
        help_texts = {
                'email': 'Введите вашу почту',
                'name': 'Используется для брони',
                'password1': 'Введите ваш пароль',
                'password2': 'Повторите ваш пароль',
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
