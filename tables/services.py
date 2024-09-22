from tables.models import Table


def reserve_end():
    tables = Table.objects.filter(is_reserved=True)

    for table in tables:
        if table.time_of_reserve:
            if table.time_end_reserve > timezone.now():
                table.is_reserved = False
                table.client = None
                table.time_of_reserve = None
                table.time_end_reserve = None
                table.save()
