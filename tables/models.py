from django.db import models
from users.models import User


class Table(models.Model):

    table_num = models.PositiveIntegerField(verbose_name='Номер столика')
    is_reserved = models.BooleanField(default=False, verbose_name='Признак брони')
    time_of_reserve = models.DateTimeField(verbose_name='Время брони')
    client = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Держатель брони', null=True, blank=True)

    class Meta:
        verbose_name = 'столик'
        verbose_name_plural = 'столики'

        def __str__(self):
            return f'Столик номер {self.table_num}'


