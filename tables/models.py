from django.db import models
from users.models import User
NULLABLE = {"blank": True, "null": True}


class Table(models.Model):

    table_num = models.PositiveIntegerField(verbose_name='Номер столика')
    is_reserved = models.BooleanField(default=False, verbose_name='Признак брони')
    time_of_reserve = models.DateTimeField(help_text='Введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ',
                                           verbose_name='Время начала брони', **NULLABLE)
    time_end_reserve = models.DateTimeField(help_text='Введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ',
                                            verbose_name='Время конца брони', **NULLABLE)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Держатель брони', **NULLABLE)
    user_phone = models.CharField(max_length=15, verbose_name='Телефон клиента', **NULLABLE)
    user_name = models.CharField(max_length=50, verbose_name='Имя клиента', **NULLABLE)

    class Meta:
        verbose_name = 'столик'
        verbose_name_plural = 'столики'

        def __str__(self):
            return f'Столик номер {self.table_num}'
