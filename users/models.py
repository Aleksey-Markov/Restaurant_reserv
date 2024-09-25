from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    модель клиента
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=12, verbose_name='Телефон клиента')
    name = models.CharField(max_length=50, verbose_name='Имя клиента')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

        def __str__(self):
            return f'{self.name} - {self.phone}'
