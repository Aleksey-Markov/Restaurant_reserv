from django.contrib import admin
from tables.models import Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
                    'id', 'table_num', 'client', 'user_name',
                    'user_phone', 'is_reserved', 'time_of_reserve',
                    'time_end_reserve'
                    )
