from tables.models import Table
from users.models import User
from django.utils import timezone


def reserve_end():
    tables = Table.objects.filter(is_reserved=True)

    for table in tables:
        if table.time_end_reserve < timezone.now():
            table.is_reserved = False
            table.client = None
            table.user_phone = None
            table.user_name = None
            table.time_of_reserve = None
            table.time_end_reserve = None
            table.save()
