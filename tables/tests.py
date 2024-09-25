from django.test import TestCase

from tables.models import Table


class TableTest(TestCase):

    def test_table_update(self):
        table = Table(1, False)
        self.assertEqual(table.table_num, 1)
        self.assertequal(table.is_reserved, False)