# Generated by Django 5.1.1 on 2024-09-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_alter_table_time_of_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя клиента'),
        ),
        migrations.AddField(
            model_name='table',
            name='user_phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон клиента'),
        ),
    ]
