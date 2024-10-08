# Generated by Django 5.1.1 on 2024-09-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_num', models.PositiveIntegerField(verbose_name='Номер столика')),
                ('is_reserved', models.BooleanField(default=False, verbose_name='Признак брони')),
                ('time_of_reserve', models.DateTimeField(verbose_name='Время брони')),
            ],
            options={
                'verbose_name': 'столик',
                'verbose_name_plural': 'столики',
            },
        ),
    ]
