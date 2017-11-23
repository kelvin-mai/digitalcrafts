import unittest
from pool_table import PoolTable
from pool_table import Tables
import os

class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.tables = Tables()
        self.pool_table = PoolTable('test',True,11,30)
        self.tables.add_table(self.pool_table)
        # print 'setUp'

    # testing PoolTable methods
    def test_pool_table_dict(self):
        self.assertTrue(
            isinstance(self.pool_table.to_dictionary(), dict)
        )
    def test_pool_table_occupied(self):
        self.assertTrue(
            isinstance(self.pool_table.is_occupied(), bool)
        )
    def test_pool_table_checkin(self):
        self.assertTrue(
            isinstance(self.pool_table.checkin(), float)
        )

    # testing Tables methods
    def test_tables_list(self):
        self.assertTrue(
            isinstance(self.tables.to_dictionary(), list)
        )

unittest.main()
