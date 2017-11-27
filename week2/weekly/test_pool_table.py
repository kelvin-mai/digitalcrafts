import unittest
from pool_table import PoolTable
from pool_table import Tables
import os

class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.tables = Tables()
        self.filename = 'test.json'
        if os.path.isfile(self.filename):
            self.tables.load(self.filename)
        else:
            for i in range(12):
                self.tables.add_table(i)
        self.tables.tables[0].checkout()

    # testing PoolTable methods
    def test_pool_table_dict(self):
        self.assertTrue(
            isinstance(self.tables.tables[0].to_dictionary(), dict)
        )
    def test_pool_table_occupied(self):
        self.assertTrue(
            isinstance(self.tables.tables[0].is_occupied(), bool)
        )
    def test_pool_table_checkin(self):
        self.assertTrue(
            isinstance(self.tables.tables[0].checkin(), float)
        )

    # testing Tables methods
    def test_tables_list(self):
        self.assertTrue(
            isinstance(self.tables.to_dictionary(), list)
        )
    def test_tables_dump(self):
        self.tables.dump(self.filename)
        self.assertTrue(
            os.path.isfile(self.filename)
        )

unittest.main()
