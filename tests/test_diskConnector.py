from unittest import TestCase
from oop.disc_connector import DiskConnector
from oop.console_query import ConsoleQuery

__author__ = 'szemek'


class TestDiskConnector(TestCase):
    def setUp(self):
        cq = ConsoleQuery(False)
        self._dc = DiskConnector(cq)

    def test_disks_names(self):
        print self._dc.disks_names()
        self.assertGreater(self._dc.disks_names(), 0, "Impossible! You have disks have no names:)")

    def test_disks_count(self):
        self.assertGreater(self._dc.disks_count(), 0, "Impossible! You have no disks:)")

    def test_disk_details(self):
        print self._dc.disk_details(1)
        result = self._dc.disk_details(1)
        self.assertTrue(result, '(\(\'name:)(.*)')